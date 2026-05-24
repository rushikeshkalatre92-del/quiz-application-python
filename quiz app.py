questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used in Python?",
        "options": ["A. Java", "B. English", "C. C++", "D. Binary"],
        "answer": "B"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    }
]

score = 0

print("Welcome to Quiz Application")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")

print("\nQuiz Completed")
print("Your Final Score:", score)