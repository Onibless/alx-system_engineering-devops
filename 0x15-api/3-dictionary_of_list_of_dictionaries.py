#!/usr/bin/python3
"""importing project modules
"""
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users'
    file_path = "todo_all_employees.json"
    employee_tasks = {}
    er = requests.get(url)
    employees = er.json()
    for employee in employees:
        employee_id = employee.get('id')
        employee_name = employee.get('username')
        task_url = f"{url}/{employee_id}/todos"
        tr = requests.get(task_url)
        tasks = tr.json()
        employee_tasks[employee_id] = []
        for task in tasks:
            employee_tasks[employee_id].append(
                {"username": employee_name,
                 "task": task.get("title"),
                 "completed": task.get("completed")})
        with open(file_path, 'w') as f:
            json.dump(employee_tasks, f)
