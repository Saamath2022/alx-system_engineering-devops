#!/usr/bin/python3

import requests

def get_employee_data(employee_id):
    
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    data = response.json()
    
    total_tasks = len(data)
    completed_tasks = sum(1 for task in data if task["completed"])
    employee_name = data[0]["userId"]
    return {
        "name": employee_name,
        "total_Wuese": total_tasks,
        "completed_Wuese": completed_tasks,
        "tasks": data
    }
