from kafka import KafkaConsumer
import json
import pickle
import numpy as np
from kafka import TopicPartition
import warnings
warnings.filterwarnings('ignore')
from threading import *


#Function for data deserialization
def json_deserializer(data):
    return json.loads(data.decode('utf-8'))

# Importing Model
rf_clf = pickle.load(open('model/rf_model.pkl', 'rb'))

# Creating Consumer
consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'],
                        auto_offset_reset="earliest",
                        group_id='group_1',
                        value_deserializer=json_deserializer)


topic = TopicPartition('project5', 0)


consumer.assign([topic])


count_cash_in = 0
count_cash_out = 0
count_debit = 0
count_payment = 0
count_transfer = 0

count_non_fraud = 0
count_fraud = 0
result = []

class consume(Thread):
    def run(self):
        for message in consumer:
            result.append(rf_clf.predict(np.array(message[6][:-1]).reshape(-1,4)))
            if result[-1] == 1:
                global count_fraud
                count_fraud += 1
            else:
                global count_non_fraud
                count_non_fraud += 1

            if message[6][0] == 0:
                global count_cash_in
                count_cash_in += 1
            elif message[6][0] == 1:
                global count_cash_out
                count_cash_out += 1
            elif message[6][0] == 2:
                global count_debit
                count_debit += 1
            elif message[6][0] == 3:
                global count_payment
                count_payment += 1
            else:
                global count_transfer
                count_transfer += 1


