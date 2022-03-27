# v0.2

import os
import sys
from price import get_price
from config import Config

def main():
    host_v = os.popen(Config.base_cmd + ' host -v').readlines()
    n = 1
    for e in host_v:
        if n == 22:
            minstorageprice = e.split()[1]
            break
        n += 1
    reference_price = get_price()
    if reference_price == 'no data':
        sys.exit()
    target_scp_price = str(round(float(reference_price) * 0.994, 3))
    print(f'Target price {target_scp_price}')
    print(f'Current price {minstorageprice}')

    if minstorageprice == target_scp_price:
        print(f'No change')
    else:
        print(f"Changing price to {target_scp_price}", flush=True)
        os.system(Config.base_cmd + ' host config minstorageprice ' + str(target_scp_price) + 'SCP')
        os.system(Config.base_cmd + ' host config collateral ' + str(target_scp_price) + 'SCP')
        # os.system(Config.base_cmd + ' host -v')

if __name__ == '__main__':
    main()
