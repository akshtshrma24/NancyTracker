import json
from datetime import date
import constants
import os

import requests


def getAndPostData():
    response = requests.get(
        'https://phx.unusualwhales.com/api/senate_stocks/Nancy%20Pelosi',
        headers=constants.HEADERS_GET_DATA)
    for item in response.json()['senate_stocks']:
        if (str(date.today()) in str(item['filed_at_date'])):
            data = f"{item['txn_type']} {item['symbol']} {item['filed_at_date']}"
            if (not isInside(data)):
                postData(data)


def isInside(check):
    response = requests.post(
        'http://localhost:8086/query',
        params=constants.PARAMS,
        headers=constants.HEADERS_INFLUX,
        data=constants.DATA_QUERY)
    if (response.text ==
            '{"results":[{"statement_id":0}]}' or check not in response.text):
        return False
    return True


def postData(toSend):
    headers = {'Content-Type': 'application/x-www-form-urlencoded', }
    params = {'db': 'mydb', }
    toSend = f'stockHist,mytag=Nancy fullTransaction="{toSend}"'
    response = requests.post(
        'http://localhost:8086/write',
        params=params,
        headers=headers,
        data=toSend)
