# Log Classification System

A multi-tiered log classification system that uses regex patterns, BERT embeddings, and LLM-based classification to categorize system log messages.

## 🌟 Features

- **Multi-tiered Classification**: Uses regex → BERT → LLM fallback strategy
- **FastAPI REST API**: Easy-to-use HTTP endpoints for log classification
- **Batch Processing**: Classify single or multiple logs at once
- **Pre-trained Models**: Uses sentence-transformers and scikit-learn
- **LLM Integration**: Groq API for complex/legacy log classification

## 📋 Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- Groq API key (for LLM classification)

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/utkarshhzz/Log_Classification.git
cd Log_Classification
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## 📊 Project Structure

```
Log_Classification/
├── main.py                    # FastAPI application
├── classify.py                # Main classification logic
├── processor_regex.py         # Regex-based classifier
├── processor_bert.py          # BERT-based classifier
├── processor_llm.py           # LLM-based classifier
├── models/
│   └── log_classifier.joblib  # Pre-trained ML model
├── training/
│   ├── training.ipynb         # Model training notebook
│   └── dataset/
│       └── synthetic_logs.csv # Training dataset
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables
```

## 🎯 Usage

### Running the FastAPI Server

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### API Endpoints

#### 1. Classify Single Log
```bash
POST /classify
```

**Request Body:**
```json
{
  "source": "System",
  "log_message": "User user123 logged in."
}
```

**Response:**
```json
{
  "source": "System",
  "log_message": "User user123 logged in.",
  "classification": "User Action"
}
```

#### 2. Classify Batch Logs
```bash
POST /classify/batch
```

**Request Body:**
```json
{
  "logs": [
    ["System", "User user123 logged in."],
    ["System", "Backup started at 2024-06-01 02:00 AM"]
  ]
}
```

**Response:**
```json
{
  "results": [
    {
      "source": "System",
      "log_message": "User user123 logged in.",
      "classification": "User Action"
    },
    {
      "source": "System",
      "log_message": "Backup started at 2024-06-01 02:00 AM",
      "classification": "System Notification"
    }
  ]
}
```

#### 3. Health Check
```bash
GET /health
```

### Command Line Usage

You can also run the classifier directly:

```bash
python classify.py
```

Or test individual processors:

```bash
python processor_regex.py
python processor_bert.py
python processor_llm.py
```

## 🔧 Classification Logic

The system uses a three-tiered approach:

1. **For LegacyCRM logs**: Directly uses LLM classification
2. **For other logs**:
   - First tries regex pattern matching
   - If no match, uses BERT embeddings with ML classifier
   - Falls back to LLM if needed

## 📝 Log Categories

- **Authentication**: Login/logout events
- **Backup**: Backup operations
- **Update**: System updates
- **File Operation**: File uploads/downloads
- **System Maintenance**: Cleanup, reboots
- **User Action**: User-initiated actions
- **Account Management**: Account creation/deletion
- **Other/Unclassified**: Unknown log types

## 🤖 Model Training

To retrain the BERT classifier:

1. Open `training/training.ipynb`
2. Ensure dataset is in `training/dataset/synthetic_logs.csv`
3. Run all cells to train and save the model
4. Model will be saved to `models/log_classifier.joblib`

## 🌐 Example cURL Commands

**Single Log Classification:**
```bash
curl -X POST "http://localhost:8000/classify" \
  -H "Content-Type: application/json" \
  -d '{"source": "System", "log_message": "User user123 logged in."}'
```

**Batch Classification:**
```bash
curl -X POST "http://localhost:8000/classify/batch" \
  -H "Content-Type: application/json" \
  -d '{"logs": [["System", "User user123 logged in."], ["System", "Backup started"]]}'
```

## 🔐 Security Notes

- Keep your `.env` file secure and never commit it to version control
- The `.gitignore` file is configured to exclude sensitive files
- Consider adding authentication for production deployments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Utkarsh Kumar**
- GitHub: [@utkarshhzz](https://github.com/utkarshhzz)

## 🙏 Acknowledgments

- Sentence Transformers for BERT embeddings
- Groq for LLM API
- FastAPI for the web framework
