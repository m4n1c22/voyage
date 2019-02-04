from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('fahr_plan.html')

@app.route('/', methods=['POST'])
def my_form_post():
    voyage_src = request.form['src']
    voyage_dest = request.form['dest']
    fahrttag = request.form['fahrttag']
    processed_text = str("From: ") + voyage_src + str(" To ") + voyage_dest + str(" on ") + fahrttag
    return processed_text
