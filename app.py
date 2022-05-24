from flask import Flask, request, render_template, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "horsey90"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def home_survey():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('main_survey.html', title=title, instructions=instructions)

@app.route('/questions/<question_num>')
def question_page(question_num):
    cur_question = satisfaction_survey.questions[int(question_num)]
    choices = cur_question.choices
    question_text = cur_question.question
    return render_template('questions.html', choices=choices, question_text=question_text)

@app.route('/answer', methods=['POST'])
def answer():
    return "got here"