import random
import json


def load_questions(filename="questions.json"):
    with open(filename, "r") as file:
        questions = json.load(file)
    return questions

def run_quiz(questions):
    random.shuffle(questions)  
    score = 0
    
  
    num_questions = min(200, len(questions))  
    
    for i, question in enumerate(questions[:num_questions], start=1):
        print(f"Question {i}: {question['question']}")
        for choice in question['choices']:
            print(choice)
        
       
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        
       
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}\n")

  
    print(f"Your final score is {score} out of {num_questions}.")


questions = load_questions()  
run_quiz(questions)           
