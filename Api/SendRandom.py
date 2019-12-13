import csv
import json
import random
import requests
import re


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
    if month in (1, 3, 5, 7, 8, 10, 12):
        day = random.randint(1, 31)
    elif month == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    date = str(year) + '-' + str(month) + '-' + str(day) + ' ' + str(hour) + ':' + str(minute) + ':' + str(second)
    return date


withDate = False

with open('..\CSV\pollenchart.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    with open('json_file.json', 'w') as jsonfile:
        out = json.dumps([make_record(row) for row in reader])
        jsonfile.write(out)

with open('json_file.json', 'r') as jsonfile:
    print('results:')
    dump = json.load(jsonfile)
    counter = 1
    while counter <= 1000:
        choice = random.choice(dump)
        if withDate:
            dice = 1
            choice["dateCreated"] = random_date()
        else:
            dice = random.randint(1, 10000000)
        if dice == 1:
            print(str(counter) + ':')
            send_request(choice)
            counter += 1
