import csv
import json
import random
from datetime import datetime

import requests
import re
from datetime import datetime
from termcolor import colored
import time


def make_record(row):
    return {
        "plantName": row["Plant name EN"],
        "hex": row["HEXColor"],
        "rgb": (row["Red"] + "," + row["Green"] + "," + row["Blue"])
    }


def send_request(json_dict):
    try:
        url = 'http://localhost:8090/pollen'
        payload = json_dict
        headers = {'content-type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(colored(response.text, 'green'))
    except ValueError as ve:
        print(colored("# Too bad, connection with database crashed! But no worries, I will continue it! #", 'white', 'on_red'))
        print(colored(ve.values, 'red'))
        time.sleep(3)
        pass


def random_date():
    year = random.randint(datetime.now().year - 5, datetime.now().year)
    month = random.randint(4, 11) # Bees are active between April and November
    day = random.randint(1, 31)
    hour = random.randint(7, 12) # Bees mostly active in the morning
    if hour == 12:
        hour = random.randint(15, 18) # Sometimes in the late afternoon
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    # Check if the date is valid
    try:
        date = str(year) + '-' + add_zero(month) + '-' + add_zero(day) + ' ' + add_zero(
            hour) + ':' + add_zero(minute) + ':' + add_zero(second)
        datetime(year, month, day, hour, minute, second)
    except ValueError as ve:
        print(colored(f"# date '{date}' is invalid, because {ve} #", 'red'))
        return random_date()  # Date is invalid, get another date!

    if datetime(year, month, day, hour, minute, second) > datetime.now(): # Prevent future dates
        return random_date()
    else:
        return date  # Date is valid!

def add_zero(number):
    if number < 10:
        return "0" + str(number)
    return str(number)


useRandomDate = False # if True, then random dates in the fast rate, else current date in the slow rate

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
    while counter <= 2000: # maximum amount of sending requests
        choice = random.choice(flowers)
        if useRandomDate:
            choice["dateCreated"] = random_date()
        else:
            dice = random.randint(1, 5000000) # random waiting time, more dice amount means longer waiting
        if dice == 1:
            print(colored(str(counter) + ':', 'white', 'on_green'))
            send_request(choice)
            counter += 1
