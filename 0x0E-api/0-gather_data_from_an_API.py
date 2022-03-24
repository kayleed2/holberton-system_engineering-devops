#!/usr/bin/python3
"""Uses a REST API to retrieve information"""
import requests
from os import sys


try:
    user_id = sys.argv[1]
    id = int(user_id)

except ValueError:
    print("ID not INT")

user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id))
name = user.json()["name"]

todos = requests.get("https://jsonplaceholder.typicode.com/todos")

all = 0
complete = 0

for k in todos.json():
    if k['userId'] == id:
        all += 1
    if k['userId'] is id and k['completed'] is True:
        complete += 1

print("Employee {} is done with tasks({}/{}):".format(name, complete, all))

for k in todos.json():
    if k['userId'] is id and k['completed'] is True:
        print("\t {}".format(k['title']))
