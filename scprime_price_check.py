# v0.9

import os
import sys
from urllib import request
import requests
from requests.structures import CaseInsensitiveDict
import json
from config import Config


def get_storageprice():
    r = requests.get('https://api.scpri.me/api/rest/suggestedsettings')
    r = r.json()
    storageprice = float(r['network_suggestedsettings'][0]['minstorageprice']) * 4320 / 1000000000000000
    print(f'The current suggested price is {(storageprice)}SCP')
    return storageprice

def main():
    host_v = os.popen(Config.base_cmd + ' host -v').readlines()
    n = 1
    for e in host_v:
        if n == 22:
            minstorageprice = e.split()[1]
            break
        n += 1
    reference_price = get_storageprice()

    if reference_price == 'no data':
        sys.exit()
    target_scp_price = str(round(float(reference_price) * 0.98, 3))
    print(f'Target price {target_scp_price}', flush=True)
    print(f'Current price {minstorageprice}', flush=True)

    if minstorageprice == target_scp_price:
        print(f'No change', flush=True)
    else:
        print(f"Changing price to {target_scp_price}", flush=True)
        os.system(Config.base_cmd + ' host config minstorageprice ' + str(target_scp_price) + 'SCP')
        os.system(Config.base_cmd + ' host config collateral ' + str(target_scp_price) + 'SCP')
        # os.system(Config.base_cmd + ' host -v')

if __name__ == '__main__':
    main()
