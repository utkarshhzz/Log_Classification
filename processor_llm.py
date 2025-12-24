from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq=Groq()

def classify_with_llm(log_message):
    prompt=f"""Classify the following log message into one of the categories:
    'Authentication', 'Backup', 'Update', 'File Operation',
    'System Maintenance', 'User Action', 'Account Management',
    or 'Other'.(if you cannot figure out a category return "Unclassified")
    Only add the category name,no preamble
    Log message: "{log_message}"
    """
    chat_completion=groq.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content":prompt,
        }
    ]
    )
    return chat_completion.choices[0].message.content


if __name__=="__main__":
    print(classify_with_llm("User user123 logged in."))
    print(classify_with_llm("Backup started at 2024-06-01 02:00 AM"))
    print(classify_with_llm("Th 'ReportGenerator' module will be retired in version 2.0."))