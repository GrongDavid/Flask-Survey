from flask import Flask, request, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "horsey90"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/begin', methods=['POST'])
def begin_survey():
    session['responses'] = []
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('main_survey.html', title=title, instructions=instructions)

@app.route('/questions/<question_num>')
def question_page(question_num):
    responses = session.get('responses')

    if(len(responses) != int(question_num)):
        flash('invalid question order/number')
        return redirect(f'/questions/{len(responses)}')

    cur_question = satisfaction_survey.questions[int(question_num)]
    choices = cur_question.choices
    question_text = cur_question.question

    return render_template('questions.html', choices=choices, question_text=question_text)

@app.route('/answer', methods=['POST'])
def answer():
    choice = request.form['answer']
    responses = session['responses']
    responses.append(choice)
    session['responses'] = responses

    if(len(responses) == len(satisfaction_survey.questions)):
        return redirect('/finished')
    else:
        return redirect(f'/questions/{len(responses)}')

@app.route('/finished')
def finished():
    return render_template('finished.html')
