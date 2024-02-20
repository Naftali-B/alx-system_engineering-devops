#!/usr/bin/python3
'''
Makes a get request to a REST API
'''

import requests
import sys

def get_employee_todo_progress(employee_id):
    '''
    Retrieves employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing employee name, number of completed tasks, and total number of tasks.
    '''
    url = 'https://jsonplaceholder.typicode.com/'
    user_data = requests.get(url + 'users/{}'.format(employee_id)).json()
    user_tasks = requests.get(url + 'todos', params={'userId': employee_id}).json()
    completed_tasks = [task.get('title') for task in user_tasks if task.get('completed')]
    return user_data.get('name'), len(completed_tasks), len(user_tasks)

def display_todo_progress(employee_id):
    '''
    Displays employee TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    '''
    todo_progress = get_employee_todo_progress(employee_id)
    if not todo_progress:
        print("Employee with ID {} not found.".format(employee_id))
        return
    employee_name, completed_tasks, total_tasks = todo_progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    [print('\t{}'.format(title)) for title in completed_tasks]

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    display_todo_progress(employee_id)
