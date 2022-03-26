# scprime_price_check

This script will get the price of SCP and update SCP/TB to a target price, defined in the script, if the difference is greater than a percentage also defined in the script.

To install it you need to clone the repository to your system.

$ git clone https://github.com/Tacombel/scprime_price_check.git

$ cd scprime_price_check

Then edit the scprime_price_check.py and chabge the target price, the tolerance and base_cmd to your needs. I am using 3.9, 0.5. As we follow the xa-miners, if you use a value to close to the standard 4.0$, some scans you will be above the limit, so better to lose some rent than to lose the incentives.

You need to edit the base_cmd to what you would be using to launch spc outside its directory. So something like '/var/lib/spc'. This is an example as I use docker.

Then:

$ python3 scprime_price_check.py

---

## Instructions for Windows (no Python experience)

- Download Python
  - Go to https://www.python.org/downloads/release/python-379/ and download the executable installer for x64 or x86
  - Install it
  - Restart the computer
- Download the repo as a zip file
  - Extract it to your SCPrime folder
  - Rename the folder (repo) to scprime_price_check
- Edit the settings
  - Open the folder
  - Edit the file scprime_price_check.py with notepad
  - Line 8 - set the target price
  - Line 9 - set the threshold percentage (update the price if the price changes with this percent)
  - Line 10 - enter the exact directory of your spc.exe - example `base_cmd = 'D:\SCPrime\spc.exe'`
- Open CMD
  - Go to the folder where the script is (for example cd D:\SCPrime\scprime_price_check)
  - Type the command python scprime_price_check.py
  - If you see the script running, you are good to continue
- Create a new text file
  - Name it pricechecker.bat
  - Edit it with notepad
  - The file should contain three lines if the folder is located on a drive other than C, or two lines if it is in the C drive
	- cd - the location of the folder (for example cd D:\SCPrime\scprime_price_check)
	- If the file is located on another drive (not C), you should put in the drive letter followed by : (for example D:)
	- python scprime_price_check.py
You can now add this file to the task scheduler and you are good to go!

-----------------------------------------------

Donations welcome:

SCP: 29397f5ac09162c48aeea537c4950d90a6b370899a2c8054a71e82ab4954228bb63e59c56464
