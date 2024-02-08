#!/usr/bin/env python3

import pandas as pd
import json

def get_inventory():
    df = pd.read_excel('/home/vagrant/inventory.xlsx')

    inventory = {}
    
    for index, row in df.iterrows():
        group = row['group']
        host = row['host']
        user = row['user']
        passwd = row['pass']

        if group not in inventory:
            inventory[group] = {'hosts': [], 'vars': {}}
        
        inventory[group]['hosts'].append(host)
        inventory[group]['vars'] = {
            "ansible_ssh_user": user,
            "ansible_user": user,
            "ansible_sudo": "yes"
        }

    print(json.dumps(inventory))

if __name__ == '__main__':
    get_inventory()
