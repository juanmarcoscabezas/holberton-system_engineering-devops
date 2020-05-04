#!/usr/bin/python3

"""
This script uses https://jsonplaceholder.typicode.com/
for a given employee ID, returns information about his/her
TODO list progress.
"""

import requests
import sys
import csv

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        userId = sys.argv[1]
        usr_url = 'https://jsonplaceholder.typicode.com/users/{}'
        r = requests.get(usr_url
                         .format(userId))
        user = r.json()
        if user:
            todos_url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
            r = requests.get(todos_url
                             .format(userId))
            todos = r.json()
            doneTasks = 0
            todosString = ''
            with open('{}.csv'.format(userId), 'w') as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for todo in todos:
                    writer.writerow([
                                     userId, user.get('username'),
                                     todo.get('completed'),
                                     todo.get('title')])
