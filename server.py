from flask import Flask, request, redirect, session, render_template
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"
import random, datetime

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process():
    if 'activity_log' not in session:
        session['activity_log'] = []
    now = datetime.datetime.now()
    if request.form['profit'] == "Farm some crops!":
        session['total_gold'] += random.randint(1, 20)
        gold_update = "You earned gold on " + str(now)
        temp = session['activity_log']
        temp.append(gold_update)
        session['activity_log'] = temp
    elif request.form['profit'] == "Explore a cave!":
        session['total_gold'] += random.randint(1, 10)
        gold_update = "You earned gold on " + str(now)
        temp = session['activity_log']
        temp.append(gold_update)
        session['activity_log'] = temp
    elif request.form['profit'] == "Stay home!":
        session['total_gold'] += random.randint(1, 5)
        gold_update = "You earned gold on " + str(now)
        temp = session['activity_log']
        temp.append(gold_update)
        session['activity_log'] = temp
        str_length = int(len(session['activity_log']))-1
    elif request.form['profit'] == "Gamble your gold!":
        session['total_gold'] += random.randint(-50, 50)
        gold_update = "You earned gold on " + str(now) + " "
        temp = session['activity_log']
        temp.append(gold_update)
        session['activity_log'] = temp
        str_length = int(len(session['activity_log']))-1
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)