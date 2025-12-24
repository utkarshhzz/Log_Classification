import re
def classify_with_regex(log_message):
    regex_patterns={
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully.": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "User Action",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern,label in regex_patterns.items():
        if re.search(pattern,log_message,re.IGNORECASE):
            return label
    return "None"

if __name__ == "__main__":
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
        print(f"Log: {log} => Classified as: {classify_with_regex(log)}")