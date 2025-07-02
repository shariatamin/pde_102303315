import pandas as pd
import json

# Read the Iris dataset
df = pd.read_csv("Iris.csv")

# Create a list to mimic messages sent to Kafka
kafka_messages = []

for index, row in df.iterrows():
    message = row.to_dict()
    kafka_messages.append(message)

# Save to a JSON file (simulate Kafka topic data)
with open("kafka_simulated_data.json", "w") as f:
    json.dump(kafka_messages, f, indent=4)

print("✅ Simulated Kafka ingestion done. Data saved in kafka_simulated_data.json")
