#!/usr/bin/python3
"""Test cases for the API utility functions."""

import sys
import os
import unittest
from unittest.mock import patch, Mock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.api_utils import get_employee_data

class TestGetEmployeeData(unittest.TestCase):
    """Unit tests for get_employee_data function."""

@patch('modules.api_utils.requests.get')
    def test_get_employee_data(self, mock_get):
        """Test fetching employee data from the API."""
        mock_user_response_1 = Mock()
        mock_user_response_1.json.return_value = {"name": "Mathias Wuese"}
        
        mock_todos_response_1 = Mock()
        mock_todos_response_1.json.return_value = [
                {"userId": 1, "completed": True, "title": "Task 1"},
                {"userId": 1, "completed": False, "title": "Task 2"},
                {"userId": 1, "completed": True, "title": "Task 3"}
        ]
        mock_user_response_2 = Mock()
        mock_user_response_2.json.return_value = {"name": "Japhet Akegh"}
        
        mock_todos_response_2 = Mock()
        mock_todos_response_2.json.return_value = [
                {"userId": 1, "completed": True, "title": "Task A"},
                {"userId": 1, "completed": False, "title": "Task B"},
                {"userId": 1, "completed": True, "title": "Task C"}
        ]

        mock_get.side_effect = [mock_user_response_1, mock_todos_response_1 mock_user_response_2, mock_todos_response_2]
        
        employee_data = get_employee_data(1)
        
        self.assertEqual(employee_data["name"], "Mathias Wuese")
        self.assertEqual(employee_data["total_tasks"], 3)
        self.assertEqual(employee_data["completed_tasks"], 2)
        self.assertEqual(len(employee_data["completed_task_titles"]), 2)
        self.assertIn("Task 1", employee_data["completed_task_titles"])
        self.assertIn("Task 3", employee_data["completed_task_titles"])

        employee_data = get_employee_data(1)
        self.assertEqual(employee_data["name"], "Japhet Akegh")
        self.assertEqual(employee_data["total_tasks"], 3)
        self.assertEqual(employee_data["completed_tasks"], 2)
        self.assertEqual(len(employee_data["completed_task_titles"]), 2)
        self.assertIn("Task A", employee_data["completed_task_titles"])
        self.assertIn("Task B", employee_data["completed_task_titles"])

if __name__ == '__main__':
    unittest.main()
