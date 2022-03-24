#!/usr/bin/python3
"""Uses a REST API to retrieve information"""
import requests
import csv
from os import sys


try:
    user_id = sys.argv[1]
    id = int(user_id)

except ValueError:
    print("ID not INT")

user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id))
name = user.json()["name"]
username = user.json()["username"]
todos = requests.get("https://jsonplaceholder.typicode.com/todos")

file = user_id + ".csv"

with open(file, 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for k in todos.json():
        if k['userId'] == id:
            data = [k['userId'], username, k['completed'], k['title']]
            writer.writerow(data)
