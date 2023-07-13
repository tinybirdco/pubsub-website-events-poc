# pubsub-website-events-poc

This repo contains an ecommerce demo that simulates a live stream of website user events, including 1) viewing products, 2) putting those into a cart, and 3) purchasing them. Using a Python script, these three event types are published to a Pub/Sub stream and consumed into a Tinybird Data Source. Once in Tinybird, these events are fed into multiple Pipes to generate daily and hourly rollups of event counts and generate API Endpoint responses. 

**Here are the components of this demo:**
+ A Python script that generates JSON event objects and publishes them to Google Pub/Sub. See the script [HERE](./data-generator/pubsub_json_generator.py).
+ A `encoded_messages` Data Source that stores the encoded Google Pub/Sub messages. Learn more about this project's Data Sources [HERE](./data-project/datasources/README.md). 
+ A `decoded_events` Pipe the decodes the JSON event objects from the messages and materializes a `events_mv` Data Source. This Data Source represents our fundamental 'table' of event objects. See its definition and schema [HERE](./data-project/pipes/decoded_events.pipe).
+ A `products` Data Source that stores product metadata including model, brand, category, and price attributes. See its schema [HERE](./data-project/datasources/products.datasource).
+ A set of Pipes that populate the Materialized Views used to generate daily and hourly rollups of event type counts. See [HERE](./data-project/pipes/).
 + A set of Pipes used to publish API Endpoints to list events and rank 'top' products. To see all the API Endpoints, see [HERE](./data-project/endpoints/).
+ A Grafana dashboard that consumes several API Endpoints. To learn more about building with Grafana, see [HERE](./dashboard/README.md).
+ Related to Grafana, the [Pipes folder](./data-project/pipes/) contains two API Endpoints for pulling product `brand` and `category` options from the `products` table to the Grafana UI. 


## Ingesting Pub/Sub data

For this demo, Google Pub/Sub is used to push messages to Tinybird. The messages arrive with an encoded 'message_data' value with encoded `event` objects. These are JSON objects that describe the upstream 'view', 'cart', and 'sale' events. 

For this demo, we specifically wanted to work with "very large" JSON objects. In this case we used this [example JSON object](./event-object/event-example.json). This static object is appended to a dynamic event object created in the script. The script generates a randomized event object with these attributes:

```python
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
```

#### Setting up your Pub/Sub feed: 

* Create a Pub/Sub topic ID and have your project ID handy. 

* Use this [Python script](./data-generator/pubsub_json_generator.py) to create JSON `event` objects and publish them to Google Pub/Sub. 

```python
from google.cloud import pubsub_v1
topic_path = publisher.topic_path(project_id, topic_id)
future = publisher.publish(topic_path, data)
```
* Setting up a Google Pub/Sub **push** subscription to write the encoded data to Tinybird using the Events API. 

For more details, see our [Ingest from Google Pub/Sub](https://www.tinybird.co/docs/guides/ingest-from-google-pubsub.html) guide.

## Generating daily and hourly rollups of event data

Inspired by the concepts shared in the [Roll up data with Materialized Views](https://www.tinybird.co/blog-posts/roll-up-data-with-materialized-views) blog post, this demo uses Materialized Views to generate daily and hourly event type totals. Here, we are assuming that those two time aggregations will lead to useful analysis. For this demo, simple plots of hourly event totals were included in the dashboard. 

As new 'view', 'cart', and 'sale' events arrive in the events_mv Data Source, their event types are rolled up incrementally by SQL Pipes into two different `daily_events_mv` and `hourly_events_mv` Data Sources. From there, you can build Pipes and publish API Endpoints. 

As stated in that blog post, "When you use Materialized Views, you can create new Data Sources containing pre-aggregated time series metrics, and query those again and again. The logic gets implanted in your data pipeline, and aggregations get updated automatically as new data is ingested."

To learn more about Materialized Views, see our [documentation](https://www.tinybird.co/docs/concepts/materialized-views.html).

