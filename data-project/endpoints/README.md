
**Publishing as API Endpoints**
+ `product_events` - This API Endpoint returns product events in reverse-chronological order. It supports custom time ranges and filtering by product category and brand. This pipe joins the real-time event feed with the product table, and is used to generate responses to [tinybird.co/v0/pipes/product_events](https://api.us-east.tinybird.co/endpoint/t_d4da9dd51fce4a06b88823231f70f465?token=p.eyJ1IjogIjRhM2M2M2Y2LWVhNTMtNDJkMi1iZDcxLTBmNDQxOGU5YWUxZiIsICJpZCI6ICIzZjM3ZDZiNS02MzIxLTQyMTctYTM2Ny0yMGRhY2E3ZTE4Y2QifQ.fp7hOR2CPmZ2I9aVi0mIlVEjmPV_hvcRCQ0gXThBpo8) requests. 

+ `top_products` - This API Endpoint returns 'top products' ranked by 'total sales' (price times the number of 'sale' events). It supports custom time ranges and filtering by product category and brand. This pipe joins the real-time event feed with the product table, and is used to generate responses to [tinybird.co/v0/pipes/top_products](https://api.us-east.tinybird.co/endpoint/t_a87ec50dd48f46f79a62e1bd3031dbdd?token=p.eyJ1IjogIjRhM2M2M2Y2LWVhNTMtNDJkMi1iZDcxLTBmNDQxOGU5YWUxZiIsICJpZCI6ICIxMDNiNTE4MC0yMGNmLTRjM2ItOTQyZS1kZGNhMTZjNDMyOGMifQ.-SbVnHpRm5BxAcUCxn4iZpvjw1Z5JsPPge4LVq9dzwI) requests. 

+ `event_counts` - Returns a single row of [event type totals](https://api.us-east.tinybird.co/v0/pipes/event_counts.json?token=p.eyJ1IjogIjRhM2M2M2Y2LWVhNTMtNDJkMi1iZDcxLTBmNDQxOGU5YWUxZiIsICJpZCI6ICIxOWNhYzM3NC1jNmYyLTQ2ZmYtYTM4OS1jZDg0MjA2ZDBjYzAifQ.V4icu0Mzwt4u2aD0AFmLROgMmFLjG9CS3s0xMvE30lE) for the requested time range. The default time range is one week. 

+ `hourly_by_product` - A work in progress to expand the event count rollups and filter by product attributes. 

#### API Endpoints to serve option data to client requests 

For this demo, the Grafana dashboard is calling these for rendering UI dropdown controls for filtering on these attributes. 

+ `api_brand`

+ `api_category`


