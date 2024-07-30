#!/usr/bin/python3

import unittest
from unittest.mock import patch
from modules.api_utils import get_employee_data

class TestGetEmployeeData(unittest.TestCase):
    @patch('modules.api_utils.requests.get')
    def test_get_employee_data(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = [
                {"userId": "Wuese Mathias", "completed": True, "title": "Task 1"},
                {"userId": "Wuese Mathias", "completed": False, "title": "Task 2"},
                {"userId": "Wuese Mathias", "completed": True, "title": "Task 3"}
        ]
        mock_get.return_value = mock_response
        employee_data = get_employee_data(5)

        self.assertEqual(employee_data["name"], "Wuese Mathias")
        self.assertEqual(employee_data["total_tasks"], 3)
        self.assertEqual(employee_data["completed_tasks"], 2)
        self.assertEqual(len(employee_data["Tasks"]), 3)

if __name__ == '__main__':
    unittest.main()
