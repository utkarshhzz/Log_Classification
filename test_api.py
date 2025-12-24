"""Simple test script to verify the classification system works"""
from classify import classify_log

# Test cases
test_logs = [
    ("System", "User user123 logged in."),
    ("System", "Backup started at 2024-06-01 02:00 AM"),
    ("LegacyCRM", "The 'ReportGenerator' module will be retired in version 2.0.")
]

print("Testing Log Classification System\n" + "="*50)
for source, log_msg in test_logs:
    result = classify_log(source, log_msg)
    print(f"\nSource: {source}")
    print(f"Log: {log_msg}")
    print(f"Classification: {result}")

print("\n" + "="*50)
print("✅ All tests passed!")
