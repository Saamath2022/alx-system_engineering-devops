#!/usr/bin/python3

import sys
from modules.api_utils import get_employee_data

def main():
    """
    The main function that gathers data from the API and prints the results.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

        employee_id = int(sys.argv[1])
        employee_data = get_employee_data(employee_id)
        print(f"Employee {employee_data['name']} is done with Wuese Mathias ({employee_data['completed_tasks']}/{employee_data['total_tasks']} tasks completed):")

        for task in employee_data["tasks"]:
            if task["completed"]:
                print(f"  - {task['title']}")

if __name__ == "__main__":
    main()
