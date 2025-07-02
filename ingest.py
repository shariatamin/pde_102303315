import pandas as pd
from kafka import KafkaProducer
import json
import time

# Read the Iris dataset
df = pd.read_csv("Iris.csv")

# Setup Kafka producer 
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Adjust if needed
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Loop through each row and send to Kafka
for index, row in df.iterrows():
    data = row.to_dict()
    producer.send('time-series-data', data)  # This is the Kafka topic
    print(f"Sent to Kafka: {data}")
    time.sleep(0.5)  # Simulate a delay (optional)

producer.close()
