#!/usr/bin/python3
"""Module containing utility functions for interacting with the API."""

import requests

def get_employee_data(employee_id):
    """Fetches employee data from the REST API and returns a dictionary.
    Args:
        employee_id (int): The ID of the employee.
    Returns:
    dict: A dictionary containing the employee's name, the number of total and completed tasks, and the titles of completed 
    """

    try:
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()
        employee_name = user_data.get("name", "Unknown")
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get("completed", False)]
        completed_count = len(completed_tasks)
        return {
                "name": employee_name,
                "total_tasks": total_tasks,
                "completed_tasks": completed_count,
                "completed_task_titles": [task.get("title", "Unknown") for task in completed_tasks]
        }
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
