#!/usr/bin/python3
"""Uses a REST API to retrieve information"""
import requests
from os import sys

if __name__ == "__main__":
    try:
        user_id = sys.argv[1]
        id = int(user_id)

    except ValueError:
        print("ID not INT")

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(id))
    name = user.json().get("name")
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    all = 0
    complete = 0

    for k in todos.json():
        if k.get('userId') == id:
            all += 1
        if k.get('userId') is id and k.get('completed') is True:
            complete += 1

    print("Employee {} is done with tasks({}/{}):".format(name, complete, all))

    for k in todos.json():
        if k.get('userId') is id and k.get('completed') is True:
            print("\t {}".format(k.get('title')))
