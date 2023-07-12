from google.cloud import pubsub_v1
from datetime import datetime
import random
import json
import time

# These are set in your Google Cloud Pub/Sub dashboard. 
project_id = 'my-demo-projects'
topic_id = 'encoded-json-events'
# These yield a Topic name of --> projects/my-demo-projects/topics/encoded-json-events

# These are hardcoded 'top level' object attributes. A hardcoded JSON object will also be appended to the object we are building.
country = 'ES'
environment = 'dev'
publisher_id = 1

# Somethings are random selections. Attributes we want to send random values for:
browsers = ['Chrome', 'Opera', 'Firefox', 'Safari']
OSs = ['Windows', 'Linux', 'OSX', 'iOS', 'Android']
products = ['6cHumpSxTvs', 'Fg15LdqpWrs', 'Zu7A1GCSjZE', 'fSdBxY0NxVI', 'xFmXLq_KJxg', '5d0cgAl5BTk', 'YY4YaHKh2jQ',
            'p8Drpg_duLw', 'sZzx0cUDX98']
event_types = ['view', 'cart', 'sale']
events_weights = [70, 43, 24]
cities = ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Malaga', 'Zaragoza', 'Bilbao', 'Alicante', 'Murcia', 'Palma de Mallorca','Toledo', 'Granada', 'Tarragona']

# Create a PubSub publisher client, where we will be writing JSON event objects.  
publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier in the form `projects/{project_id}/topics/{topic_id}`
topic_path = publisher.topic_path(project_id, topic_id)

while True:
    product_id = random.choice(products)
    units = random.randrange(1, 3, 1)
    event_type = random.choice(event_types)

    # Build object to publish on Pub/Sub topic stream.
    event = {
        'timestamp': datetime.utcnow().isoformat(),
        'publisher_id': publisher_id,
        'event': random.choices(event_types, weights=events_weights, k=1)[0],
        'product': random.choice(products),
        'browser': random.choice(browsers),
        'environment': environment,
        'country': country,
        'OS': random.choice(OSs),
        'city': random.choice(cities),  # Add randomly picked city attribute
    }

    # Import JSON file and merge its data with the event dictionary.
    # TODO: update this path to point to the JSON object you want to append.
    with open('../event-object/event.json') as file:
        json_data = json.load(file)
        event.update(json_data)

    data_str = json.dumps(event)
    print(f"[{datetime.utcnow().isoformat()}] Sending JSON encoded in utf-8: {data_str}")
    data = data_str.encode("utf-8")

    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    # print(future.result())

    # Generate a random sleep duration between 1 and 10 seconds
    # Tune to the volume you want.
    #sleep_duration = random.uniform(0.1,0.5) #Black Friday volumes
    sleep_duration = random.uniform(1,10) #More moderate volumes
    
    # Wait for the generated duration
    time.sleep(sleep_duration)