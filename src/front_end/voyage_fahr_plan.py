from flask import Flask, request, render_template

from backend_controller import Voyage_Carpool_Controller as Car_Pool_Controller

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('fahr_plan.html')

@app.route('/', methods=['POST'])
def my_form_post():
    voyage_src = request.form['src']
    voyage_dest = request.form['dest']
    beign_date = request.form['begin_date']
    end_date = request.form['end_date']
    processed_text = str("From: ") + voyage_src + str(" To ") + voyage_dest + str(" between ") + begin_date + " - " + end_date
    return processed_text
