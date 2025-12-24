from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, ConfigDict
from typing import List, Tuple
from classify import classify_log, classify
import uvicorn
import os

app = FastAPI(
    title="Log Classification API",
    description="API for classifying log messages using regex, BERT, and LLM",
    version="1.0.0"
)

# Mount static files
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LogMessage(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source": "System",
                "log_message": "User user123 logged in."
            }
        }
    )
    
    source: str
    log_message: str

class LogBatch(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "logs": [
                    ["System", "User user123 logged in."],
                    ["System", "Backup started at 2024-06-01 02:00 AM"]
                ]
            }
        }
    )
    
    logs: List[Tuple[str, str]]

class ClassificationResponse(BaseModel):
    source: str
    log_message: str
    classification: str

class BatchClassificationResponse(BaseModel):
    results: List[ClassificationResponse]

@app.get("/")
async def root():
    """Root endpoint - serves the demo UI"""
    if os.path.exists("static/index.html"):
        return FileResponse("static/index.html")
    return {
        "message": "Log Classification API",
        "version": "1.0.0",
        "endpoints": {
            "/classify": "POST - Classify a single log message",
            "/classify/batch": "POST - Classify multiple log messages",
            "/health": "GET - Health check endpoint",
            "/docs": "GET - API documentation"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Log Classification API"}

@app.post("/classify", response_model=ClassificationResponse)
async def classify_single_log(log: LogMessage):
    """
    Classify a single log message
    
    - **source**: The source of the log (e.g., "System", "LegacyCRM")
    - **log_message**: The actual log message to classify
    """
    try:
        classification = classify_log(log.source, log.log_message)
        return ClassificationResponse(
            source=log.source,
            log_message=log.log_message,
            classification=classification
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Classification error: {str(e)}")

@app.post("/classify/batch", response_model=BatchClassificationResponse)
async def classify_batch_logs(batch: LogBatch):
    """
    Classify multiple log messages at once
    
    - **logs**: List of tuples containing [source, log_message]
    """
    try:
        classifications = classify(batch.logs)
        results = [
            ClassificationResponse(
                source=source,
                log_message=log_msg,
                classification=label
            )
            for (source, log_msg), label in zip(batch.logs, classifications)
        ]
        return BatchClassificationResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch classification error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
