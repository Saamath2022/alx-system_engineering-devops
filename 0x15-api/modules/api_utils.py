#!/usr/bin/python3
import requests

def get_employee_data(employee_id):
    """
    Retrieves the todo list for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    Returns:
        dict: A dictionary containing the employee's name and a list of their tasks.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    data = response.json()
    
    total_tasks = len(data)
    completed_tasks = sum(1 for task in data if task["completed"])
    employee_name = data[0]["userId"]

    return {
            "name": employee_name,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "tasks": data
    }
