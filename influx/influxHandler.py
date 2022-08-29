import json
from datetime import date
import os

import requests

import constants as constants
from logger import *


def parseResponseCode(code):
    return int(str(code)[-5:-2])


# If it is an error it will print out an error
def isError(code, response):
    if (code > 204):
        error("Error Sending response to influx, Status: ",
              response, "\n Full Text: ", response.text)


def createDB():
    info("Creating Database if not created already")
    response = requests.post(
        'http://influxDB:8086/query',
        headers=constants.HEADERS_INFLUX,
        data=constants.CREATE_DATABASE)
    if (isError(parseResponseCode(response), response)):
        error("Got error trying to create DB")


def isInside(check):
    response = requests.post(
        'http://influxDB:8086/query',
        params=constants.PARAMS,
        headers=constants.HEADERS_INFLUX,
        data=constants.DATA_QUERY)
    if (isError(parseResponseCode(response), response)):
        error("Got error trying to create DB")
    if (response.text ==
            '{"results":[{"statement_id":0}]}' or check not in response.text):
        return False
    return True


def postData(toSend):
    headers = {'Content-Type': 'application/x-www-form-urlencoded', }
    params = {'db': 'stockHist', }
    toSend = f'stockHist,mytag=Nancy fullTransaction="{toSend}"'
    response = requests.post(
        'http://influxDB:8086/write',
        params=params,
        headers=headers,
        data=toSend)
    if (isError(parseResponseCode(response), response)):
        error("Got error trying to create DB")
    else:
        success("Posted to Influx!")
