import random
import time
from faker import Faker
import json

fake = Faker()

def generate_call_data():
    return {
        "call_id": fake.uuid4(),
        "caller_number": fake.phone_number(),
        "receiver_number": fake.phone_number(),
        "call_duration": round(random.uniform(0.5, 30.0), 2),  
        "call_timestamp": fake.date_time_this_year().isoformat(),
        "is_scam": random.choice([True, False]) 
    }

# Simulate phone calls
if __name__ == "__main__":
    start_time =time.time()
    while time.time() -start_time <10:
        call_data = generate_call_data()
        print(json.dumps(call_data))  
        time.sleep(1)  
