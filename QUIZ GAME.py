# Simple Quiz Game

# Questions and answers
questions = [
    {
        "question": "Telangana was formed as a separate on which data ?",
        "options": ["A. June 2,2014", "B. August 15,2014", "C. July 1,2014", "D. May 1,2014"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["A. J.R.R. Tolkien", "B. J.K. Rowling", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    }
]

score = 0

# Asking questions
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer was", q["answer"])

# Final score
print("\nQuiz finished!")
print("Your score is:", score, "/", len(questions))