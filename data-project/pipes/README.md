# Pipes 

Pipes in this folder are used to build Materialized Views and also decode and extract attributes from `event` JSON. 

**Streaming feed**   
+ `decoded_events` - Reads in 'raw' Pub/Sub messages from the encode_messages Data Source. The first Node decodes the `message_data` contents and writes that to an `event_data` column containing the JSON object (as a string). The second Node selects JSON attributes of interest and writes each one to its own column in the (Materialized) events_mv Data Source.
  + `encoded_messages DS` --> `decoded_events Pipe` --> `events_mv DS`

**Creating and maintaining daily and hourly rollups**
+ `make_daily_events_mv`- Reads in `events_mv` data and uses the `toStartOfDay(event_time)` and `countIfState(event = ) to materialize a `daily_events_mv` DS.
  + `events_mv DS` --> `make_daily_events_mv Pipe` --> `daily_events_mv DS`
+ `makes_hourly_events_mv` - Generates a roll-up for each hour. Same pattern as the daily rollup.  Reads in `events_mv` data and uses the `toStartOfHour(event_time)` and `countIfState(event = ) to materialize a `hourly_events_mv` DS.
  + `events_mv DS` --> `make_hourly_events_mv Pipe` -->  `hourly_events_mv DS`

