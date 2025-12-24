from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm




def classify(logs):
    labels=[]
    for source,log_msg in logs:
        labels.append(classify_log(source,log_msg))
    return labels

def classify_log(source,log_message):
    if(source=="LegacyCRM"):
        label=classify_with_llm(log_message)
    else:
        
        label=classify_with_regex(log_message)
        if label is None:
            label=classify_with_bert(log_message)
    return label




if __name__=="__main__":
    logs=[
        ("System","User user123 logged in."),
        ("System","Backup started at 2024-06-01 02:00 AM"),
        ("System","System updated to version 2.1.0"),
        ("System","File report.pdf uploaded successfully."),
        ("System","Disk cleanup completed successfully."),
        ("System","System reboot initiated by user admin"),
        ("System","Account with ID 456 created by user789"),
        ("System","Unrecognized log message format."),
        ("LegacyCRM", "The 'ReportGenerator' module will be retired in version 2.0.")
    ]
    
    print("Classifying logs...\n")
    labels = classify(logs)
    
    for (source, log), label in zip(logs, labels):
        print(f"Source: {source}")
        print(f"Log: {log}")
        print(f"Classification: {label}\n")
   