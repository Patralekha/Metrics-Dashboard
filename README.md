# Metrics-Dashboard
Project 3: Observability


**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for the three components. Copy and paste the output or take a screenshot of the output and include it here to verify the installation
![Screenshot from 2021-10-25 18-55-27](https://user-images.githubusercontent.com/46372817/138703976-16ddd7b8-2bab-4722-b209-f162265da305.png)
![Screenshot from 2021-10-25 18-55-41](https://user-images.githubusercontent.com/46372817/138704019-b4f8e10f-3b39-4eab-8cd9-21b12c98d29d.png)


## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.
![Screenshot from 2021-10-25 17-12-09](https://user-images.githubusercontent.com/46372817/138702727-d3b0a6f5-58a2-4fe6-a518-22e24f9ab96f.png)



## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.
![Screenshot from 2021-10-24 21-59-58](https://user-images.githubusercontent.com/46372817/138604607-79801a84-08b7-49f4-8e3a-721593995ce7.png)
![Screenshot from 2021-10-24 22-33-16](https://user-images.githubusercontent.com/46372817/138604740-3e455335-6f1f-44dd-926e-db0e88875d88.png)


## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.
![Screenshot from 2021-10-24 22-04-49](https://user-images.githubusercontent.com/46372817/138604621-59ab6e1e-af97-47ff-a967-e9606316b92b.png)
![Screenshot from 2021-10-17 23-46-07](https://user-images.githubusercontent.com/46372817/138604645-b00aa118-580c-4272-a7dd-c31c654abe8d.png)


## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
