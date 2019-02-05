from flask import Flask, request, render_template

from ..back_end.voyage_car_pool_controller import Voyage_Carpool_Controller as Car_Pool_Controller

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('fahr_plan.html')

@app.route('/', methods=['POST'])
def my_form_post():
    voyage_src = request.form['src']
    voyage_dest = request.form['dest']
    begin_date = request.form['begin_date']
    end_date = request.form['end_date']
    #processed_text = str("From: ") + voyage_src + str(" To ") + voyage_dest + str(" between ") + begin_date + " - " + end_date
    #return processed_text

    car_pool_obj = Car_Pool_Controller()
    avail_rides = car_pool_obj.checkAvailableRides(voyage_src, voyage_dest, begin_date, end_date)
    processed_text = str(avail_rides)
    return processed_text
