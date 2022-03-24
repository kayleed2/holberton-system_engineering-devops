#!/usr/bin/python3
"""Uses a REST API to retrieve information"""
import requests
import json
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

file = user_id + ".json"

with open(file, 'w') as f:
    Dict = {}
    Dict[id] = []
    for k in todos.json():
        if k['userId'] == id:
            dictionary = {"task": k['title'],
                          "completed": k['completed'], "username": username}
            Dict[id].append(dictionary)
    json.dump(Dict, f)
