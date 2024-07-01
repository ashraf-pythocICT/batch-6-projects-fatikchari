def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for i, (question, options, correct_option) in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question}")
        for j, option in enumerate(options, start=1):
            print(f"{j}. {option}")

        user_answer = int(input("Enter the number corresponding to your answer: "))

        if user_answer == correct_option:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_option}: {options[correct_option-1]}\n")

    print(f"You answered {score} out of {total_questions} questions correctly.")

# Example questions: (Question, [Options], Correct Option)
questions = [
    ("What is the capital of Bangladesh?", ["Dhaka", "Chittagong", "Barisal", "Khulna"], 1),
    ("What is the name of your district ?", ["Dhaka", "Chittagong", "Fatikchari", "Rajshahi"], 2),
    ("What is the national game of Bangladesh?", ["football", "kabadi", "badminton", "cricket"], 2),
]

run_quiz(questions)
