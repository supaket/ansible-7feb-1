#!/usr/bin/env python3

import csv
import json
import sys

csv_file = 'hosts.csv'

inventory = {"all": {"children": {}}}

try:
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            hostname = row['hostname']
            group = row['group']
            if group not in inventory["all"]["children"]:
                inventory["all"]["children"][group] = {"hosts": []}
            inventory["all"]["children"][group]["hosts"].append(hostname)
except Exception as e:
    print(f"Error reading CSV file: {e}")
    sys.exit(1)

if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(inventory))
elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({}))
else:
    print("Usage: {} --list or {} --host <hostname>".format(sys.argv[0], sys.argv[0]))
    sys.exit(1)

