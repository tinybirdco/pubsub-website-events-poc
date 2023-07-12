# Pipes and API Endpoints

**Streaming feed**   
+ `decoded_events` - Reads in 'raw' Pub/Sub messages from the encode_messages Data Source. The first Node decodes the `message_data` contents and writes that to an `event_data` column containing the JSON object (as a string). The second Node selects JSON attributes of interest and writes each one to its own column in the (Materialized) events_mv Data Source.
  + `encoded_messages DS` --> `decoded_events Pipe` --> `events_mv DS`

**Creating and maintaining daily and hourly rollups**
+ `make_daily_events_mv`- Reads in `events_mv` data and uses the `toStartOfDay(event_time)` and `countIfState(event = ) to materialize a `daily_events_mv` DS.
  + `events_mv DS` --> `make_daily_events_mv Pipe` --> `daily_events_mv DS`
+ `makes_hourly_events_mv` - Generates a roll-up for each hour. Same pattern as the daily rollup.  Reads in `events_mv` data and uses the `toStartOfHour(event_time)` and `countIfState(event = ) to materialize a `hourly_events_mv` DS.
  + `events_mv DS` --> `make_hourly_events_mv Pipe` -->  `hourly_events_mv DS`

**Publishing as API Endpoints**
+ `product_events` - This API Endpoint returns product events in reverse-chronological order. It supports custom time ranges and filtering by product category and brand. This pipe joins the real-time event feed with the product table, and is used to generate responses to (https://api.us-east.tinybird.co/endpoint/t_d4da9dd51fce4a06b88823231f70f465?token=p.eyJ1IjogIjRhM2M2M2Y2LWVhNTMtNDJkMi1iZDcxLTBmNDQxOGU5YWUxZiIsICJpZCI6ICIzZjM3ZDZiNS02MzIxLTQyMTctYTM2Ny0yMGRhY2E3ZTE4Y2QifQ.fp7hOR2CPmZ2I9aVi0mIlVEjmPV_hvcRCQ0gXThBpo8)[tinybird.co/v0/pipes/product_events] requests. 

+ `top_products` - This API Endpoint returns 'top products' ranked by 'total sales' (price times the number of 'sale' events). It supports custom time ranges and filtering by product category and brand. This pipe joins the real-time event feed with the product table, and is used to generate responses to (https://api.us-east.tinybird.co/endpoint/t_a87ec50dd48f46f79a62e1bd3031dbdd?token=p.eyJ1IjogIjRhM2M2M2Y2LWVhNTMtNDJkMi1iZDcxLTBmNDQxOGU5YWUxZiIsICJpZCI6ICIxMDNiNTE4MC0yMGNmLTRjM2ItOTQyZS1kZGNhMTZjNDMyOGMifQ.-SbVnHpRm5BxAcUCxn4iZpvjw1Z5JsPPge4LVq9dzwI)[tinybird.co/v0/pipes/top_products] requests. 




