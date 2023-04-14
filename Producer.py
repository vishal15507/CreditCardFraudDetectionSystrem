# Importing required packages
from kafka.admin import NewTopic, KafkaAdminClient
from kafka import KafkaProducer
import json
from time import sleep
import pandas as pd
from threading import *
from sklearn.preprocessing import LabelEncoder

#Creating new topic
topic = NewTopic(name='project5',
                num_partitions=1,
                replication_factor=1)
admin = KafkaAdminClient(bootstrap_servers='localhost:9092')
admin.create_topics([topic])

# Function for data serialization
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Importing Data
df = pd.read_csv('data/Simulation Dataset.csv')

# Data Preprocessing
df = df[['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'isFraud']]
le = LabelEncoder()
df['type'] = le.fit_transform(df['type'])

#Producing data
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                        value_serializer=json_serializer)

class produce(Thread):
    def run(self):
        for index, row in df.iterrows():
            producer.send('project5', row.to_list())
            sleep(0.5)