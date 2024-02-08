#!/usr/bin/env python3

import pandas as pd
import json

def get_inventory():
    df = pd.read_excel('/home/vagrant/inventory.xlsx')

    inventory = {}
    
    for index, row in df.iterrows():
        group = row['group']
        host = row['host']

        if group not in inventory:
            inventory[group] = {'hosts': []}
        
        inventory[group]['hosts'].append(host)

    print(json.dumps(inventory))

if __name__ == '__main__':
    get_inventory()
