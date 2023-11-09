# Define a list of questions and answers as tuples
quiz_questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is known as the 'Red Planet'?", "Mars"),
    ("What is 2 + 2?", "4"),
]

# Function to conduct the quiz
def run_quiz(questions):
    score = 0
    for question, correct_answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.")
    
    print(f"You got {score} out of {len(questions)} questions correct!")

# Run the quiz
print("Welcome to the Quiz Game!")
run_quiz(quiz_questions)