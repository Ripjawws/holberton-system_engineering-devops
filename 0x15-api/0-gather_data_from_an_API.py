#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
from sys import argv
if __name__ == "__main__":
    name = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': argv[1]})
    r = requests.get('https://jsonplaceholder.typicode.com/todos',
                     params={'userId': argv[1]})
    TOTAL_NUMBER_OF_TASKS = len(r.json())
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    for item in r.json():
        if item.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(item.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(name.json()[0].get('name'), NUMBER_OF_DONE_TASKS,
                 TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))
