#!/usr/bin/python3
"""
Module to get TODO list progress for a given employee ID and export to JSON
"""
import csv
import json
import requests


def fetch_users():
    """Fetch user data from the URL."""
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    return response.json()


def fetch_tasks():
    """Fetch task data from the URL."""
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    return response.json()


def organize_data(users, tasks):
    """Organize data into the required format."""
    # Create a dictionary for users with user_id as the key
    users_dict = {str(user['id']): user['username'] for user in users}

    # Create a dictionary for tasks, where each key is user_id
    tasks_dict = {}
    for task in tasks:
        user_id = str(task['userId'])
        task_info = {
            "username": users_dict.get(user_id, "Unknown"),
            "task": task['title'],
            "completed": task['completed']
        }
        if user_id not in tasks_dict:
            tasks_dict[user_id] = []
        tasks_dict[user_id].append(task_info)

    return tasks_dict


def main():
    """Main driver function"""
    # Fetch data
    users = fetch_users()
    tasks = fetch_tasks()

    # Organize data
    organized_data = organize_data(users, tasks)

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(organized_data, json_file)


if __name__ == "__main__":
    main()
