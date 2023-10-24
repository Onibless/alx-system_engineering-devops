#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import json
import requests
import sys


def get_user_todo_list():
    employee_id = int(sys.argv[1])
    url1 = 'https://jsonplaceholder.typicode.com/users/%s' % employee_id
    url2 = '%s/todos' % url1
    todo_list = requests.get(url2).json()
    user = requests.get(url1).json()
    completed_todo = []
    for todo in todo_list:
        if todo.get('completed') is True:
            completed_todo.append(todo.get('title'))
