from sentence_transformers import SentenceTransformer
import joblib

transformer_model=SentenceTransformer('all-MiniLM-L6-v2')



def classify_with_bert(log_message):
    
    
    #Computing embedding
    message_embedding=transformer_model.encode(log_message)
    #Loading pre-trained classifier
    clasifier_model=joblib.load('models/log_classifier.joblib')
    
    predicted_class= clasifier_model.predict([message_embedding])[0]
    
    return predicted_class


if __name__=="__main__":
    test_logs=[
        "User user123 logged in.",
        "Backup started at 2024-06-01 02:00 AM",
        "System updated to version 2.1.0",
        "File report.pdf uploaded successfully.",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user admin",
        "Account with ID 456 created by user789",
        "Unrecognized log message format."
    ]
    for log in test_logs:
        print(f"Log: {log} => Classified as: {classify_with_bert(log)}")
    