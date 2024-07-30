#!/usr/bin/python3
"""
Module to get TODO list progress for a given employee ID and export to CSV
"""
import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and the TODO list progress of an employee and exports it to CSV.

    Args:
        employee_id (int): The ID of the employee

    Returns:
        None
    """
    # Fetch user information
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')
    username = user_data.get('username')

    # Fetch user's todo list
    t_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(t_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    # Export to CSV
    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([
                employee_id,
                username,
                task.get('completed'),
                task.get('title')
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
