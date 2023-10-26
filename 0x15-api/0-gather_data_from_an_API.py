#!/usr/bin/python3
"""importing project modules
"""
import requests
from sys import argv


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/users'
    employee_id = int(argv[1])
    url = f"{base_url}/{employee_id}"
    todo_url = f"{url}/todos"
    ur = requests.get(url)
    tr = requests.get(todo_url)
    if ur.status_code == 200:
        if tr.status_code == 200:
            employee_tasks = tr.json()
            employee_name = ur.json()
            done = 0
            total = 0
            completed = []
            for task in employee_tasks:
                if task.get("completed") is True:
                    completed.append(task.get("title"))
                    done += 1
                total += 1
            print("Employee {} is done with tasks({}/{}):"
                  .format(employee_name.get('name'), done, total))
            [print(f"\t {i}")for i in completed]
