# pubsub-website-events-poc

This repo contains an ecommerce demo that simulates a live stream of website user events, including viewing products, putting those into a cart, and purchasing them. Using a Python script, these three event types are published to a Pub/Sub stream and consumed into a Tinybird Data Source. Once in Tinybird, these events are fed into multiple Pipes to generate daily and hourly rollups of event counts and generate API Endpoint responses. 

Here are the components of this demo:
+ A Python script that generates JSON event objects and publishes them to Google Pub/Sub.
+ A `encoded_messages` that stores the encoded Google Pub/Sub messages. 
+ A `decoded_events` Pipe the decodes the JSON event objects from the messages and materializes a `events_mv` Data Source. This Data Source represents our fundamental 'table' of event objects. 
+ A `products` Data Source that stores product metadata including model, brand, category, and price attributes. 
+ A set of Pipes and Data Sources that generate daily and hourly rollups of event type counts. 
+ A set of Pipes used to publish API Endpoints to list events and rank 'top' products. 
+ A Grafana dashboard that consumes several API Endpoints. 


Check [dashboard's readme](./dashboard/README.md) to see how it is configured, and [data-project's readme](./data-project/README.md) to see Tinybird resources.



