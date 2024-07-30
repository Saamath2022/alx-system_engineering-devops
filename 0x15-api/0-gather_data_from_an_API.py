#!/usr/bin/python3

import sys
from modules.api_utils import get_employee_data

def main():
    """Main function that gathers data and prints the TODO list progress."""
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    employee_data = get_employee_data(employee_id)
    if employee_data and employee_data["name"] != "Unknown":
        print(f"Employee {employee_data['name']} is done with tasks({employee_data['completed_tasks']}/{employee_data['total_tasks']}):")
        for title in employee_data["completed_task_titles"]:
            print(f"\t {title}")
        else:
            print(f"No data found for employee ID {employee_id}")

if __name__ == "__main__":
    main()
