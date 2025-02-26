import json
import random
import time
import numpy as np
from faker import Faker
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

fake = Faker()

# Generate call data
def generate_call_data():
    return {
        "call_duration": round(random.uniform(0.5, 30.0), 2),  # Call duration in minutes
        "caller_number": fake.phone_number(),
        "receiver_number": fake.phone_number(),
        "is_scam": random.choice([True, False])  # Label (target)
    }

# Collect training data
data = []
labels = []
count = 1

print("Starting call data collection...")
while count< 1000:  # Collect data for 10 seconds
    call_data = generate_call_data()
    data.append([call_data["call_duration"]])  # Using only call_duration as feature
    labels.append(call_data["is_scam"])
    count +=1

print("Call data collection completed.")

# Convert labels to numerical values (True -> 1, False -> 0)
labels = np.array(labels, dtype=int)

# Split data into training and testing sets
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Train KNN model
print("Training KNN model...")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
print("KNN model training completed.")

# Test model on new call data
test_call = [[random.uniform(0.5, 30.0)]]  # Generate random call duration
print(f"Testing with new call duration: {test_call[0][0]} minutes")
prediction = knn.predict(test_call)
print(f"Predicted Scam: {'Yes' if prediction[0] else 'No'}")
