import pandas as pd
import json

def get_inventory():
    df = pd.read_excel('inventory.xlsx')

    inventory = {}
    
    for index, row in df.iterrows():
        group = row['group']
        host = row['host']
        ip = row['ip']

        if group not in inventory:
            inventory[group] = {'hosts': [], 'ips':[]}
        
        inventory[group]['hosts'].append(host)
        inventory[group]['ips'].append(ip)

    print(json.dumps(inventory))

if __name__ == '__main__':
    get_inventory()
