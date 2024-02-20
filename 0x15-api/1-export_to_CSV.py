#!/usr/bin/python3
''' Makes a get request to a REST API and exports data in CSV format '''
import requests
import csv
from sys import argv

def export_to_csv(user_data, user_tasks):
    '''Exports user tasks to a CSV file'''
    with open('{}.csv'.format(user_data['id']), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in user_tasks:
            csv_writer.writerow([task.get('userId'),
                                 user_data.get('username'),
                                 task.get('completed'),
                                 task.get('title')])

if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: python3 {} <employee_id>".format(argv[0]))
        exit(1)

    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    
    user_data = requests.get(url + 'users/{}'.format(user_id)).json()
    if 'id' not in user_data:
        print("Employee with ID {} not found.".format(user_id))
        exit(1)
    
    user_tasks = requests.get(url + 'todos', params={'userId': user_id}).json()
    export_to_csv(user_data, user_tasks)

