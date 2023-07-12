## Dashboard details

* This definition JSON file can be imported to Grafana to provide a dashboard foundation. 
* After importing the definition file, you will need to navigate to all the visualizations and update the `token` query parameters. 
* You will also need to create your own Data Source and configure it with your Workspace URL. 
* The `tinybird-ui-apis` folder contains two Pipe definitions that provide simple API Endpoints for returning supported values for Grafana UI controls/filters. Grafana will make requests to get the strings/names for your dashboard UI. 

