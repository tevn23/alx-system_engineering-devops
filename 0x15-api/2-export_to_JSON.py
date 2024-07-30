#!/usr/bin/python3
"""
Module to get TODO list progress for a given employee ID and export to JSON
"""
import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and the TODO list progress of an employee and exports it to JSON.

    Args:
        employee_id (int): The ID of the employee

    Returns:
        None
    """
    # Fetch user information
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch user's todo list
    t_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(t_url)
    todos_data = todos_response.json()

    # Prepare data for JSON export
    tasks = []
    for task in todos_data:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks.append(task_info)

    # Create JSON structure
    json_data = {str(employee_id): tasks}

    # Write to JSON file
    json_filename = f'{employee_id}.json'
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
