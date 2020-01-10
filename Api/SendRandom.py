import csv
import json
import random
from datetime import datetime

import requests
from termcolor import colored
import time


def make_record(row):
    return {
        "plantName": row["Plant name EN"],
        "hex": row["HEXColor"],
        "rgb": (row["Red"] + "," + row["Green"] + "," + row["Blue"])
    }


def send_request(json_dict):
    url = 'http://localhost:8090/pollen'
    payload = json_dict
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


def random_date():
    year = random.randint(2014, 2019)
    month = random.randint(1, 12)
    day = random.randint(1, 31)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    # Check if the date is valid
    try:
        # year = 2015
        # month = 3
        # day = 29;
        # hour = 2
        # minute = 1
        # second = 1
        date = str(year) + '-' + add_zero(month) + '-' + add_zero(day) + ' ' + add_zero(
            hour) + ':' + add_zero(minute) + ':' + add_zero(second)
        datetime(year, month, day, hour, minute, second)
    except ValueError as ve:
        print(colored(f"# date '{date}' is invalid, because {ve} #", 'red'))
        date = random_date()  # Date is invalid, get another date!

    return date  # Date is valid!


def add_zero(number):
    if number < 10:
        return "0" + str(number)
    return str(number)


withDate = True

with open('..\CSV\pollenchart.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    with open('json_file.json', 'w') as jsonfile:
        out = json.dumps([make_record(row) for row in reader])
        jsonfile.write(out)

with open('json_file.json', 'r') as jsonfile:
    print('results:')
    dump = json.load(jsonfile)
    flowers = []
    for i in range(0, 10):
        flowers.append(random.choice(dump))

    counter = 1
    dice = 1
    while counter <= 50000:
        choice = random.choice(flowers)
        if withDate:
            choice["dateCreated"] = random_date()
        else:
            dice = random.randint(1, 100000)
        if dice == 1:
            print(str(counter) + ':')
            send_request(choice)
            counter += 1
