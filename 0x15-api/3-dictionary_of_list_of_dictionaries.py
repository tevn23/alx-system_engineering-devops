import requests
import json


def fetch_data():
    # URLs for the data
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch users and todos data
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    # Check if the requests were successful
    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data.")
        return {}

    # Parse JSON data
    users = users_response.json()
    todos = todos_response.json()

    # Organize data by user ID
    user_data = {user['id']: {'username': user['username']} for user in users}
    todo_data = {}

    for todo in todos:
        user_id = todo['userId']
        if user_id not in todo_data:
            todo_data[user_id] = []
        todo_data[user_id].append({
            "username": user_data[user_id]['username'],
            "task": todo['title'],
            "completed": todo['completed']
        })

    # Write data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_data, json_file, indent=4)


if __name__ == "__main__":
    fetch_data()
