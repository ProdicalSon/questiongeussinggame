from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import random

# Load the questions from the JSON file
def load_questions(filename="questions.json"):
    with open(filename, "r") as file:
        return json.load(file)

app = Flask(__name__)

# Global variable to hold current question and score
questions = load_questions()
random.shuffle(questions)  # Shuffle questions each time
current_question = 0
score = 0

@app.route('/')
def index():
    global current_question, score
    if current_question < len(questions):
        question = questions[current_question]
        return render_template('quiz.html', question=question, score=score)
    else:
        return redirect(url_for('result'))

@app.route('/submit', methods=['POST'])
def submit_answer():
    global current_question, score
    user_answer = request.form['answer']
    correct_answer = questions[current_question]['answer']
    
    # Check if the answer is correct and update score
    if user_answer == correct_answer:
        score += 1
    
    # Move to the next question
    current_question += 1
    
    return redirect(url_for('index'))

@app.route('/result')
def result():
    global score
    return render_template('result.html', score=score)

if __name__ == "__main__":
    app.run(debug=True)
