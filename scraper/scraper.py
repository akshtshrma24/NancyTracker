import sys
import time

from prometheus_client import start_http_server, Summary

from data import getData 
from influxHandler import * 
from logger import * 

#create Database if not already created
createDB()
    
info("Starting Scraper")
trade_made = Gauge('trade_made', '1 if she made trade 0 if she didnt in past hour')
start_http_server(5000)
# Generate some requests.
if __name__ == '__main__':
    while True:
        data = getData()
        if (data != None and not isInside(data)):
            success("Trade Made!")
            trade_made.set(1)
            postData(data)
        else:
            trade_made.set(0)
        time.sleep(int(sys.argv[1]))


# Create a metric to track time spent and requests made.


    # Start up the server to expose the metrics.