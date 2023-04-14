from flask import Flask, render_template, jsonify
from threading import *
import Consumer
import Producer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/data')
def get_data():
    count_data1 = Consumer.count_fraud
    count_data2 = Consumer.count_non_fraud
    return jsonify({
        'pie_data': [count_data1, count_data2],
        'column_data': [Consumer.count_cash_in, Consumer.count_cash_out, Consumer.count_debit, Consumer.count_payment, Consumer.count_transfer],
        'count_data1': count_data1,
        'count_data2': count_data2
    })

class dashboard(Thread):
    def run(self):
        app.run()
        
t1 = Producer.produce()
t2 = Consumer.consume()
t3 = dashboard()

t1.start()
t2.start()
t3.start()