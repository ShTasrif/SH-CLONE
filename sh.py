import requests
import os
import sys
import time

#Check Version

print("Checking For Updates...")

version = open(".version.txt")

mainversion = requests.get("https://raw.githubusercontent.com/ShTasrif/SH-CLONER/main/.version.txt")

mainversion = mainversion.text

time.sleep(0.6)

if(version==mainversion):
	print("You are using the latest version of SH-CLONER")

else:
	print("\t\tTool Update Found")
	print("\t\t  Updating Tool...")

	os.system("cd .. && rm -rf SH-CLONER && git clone https://github.com/ShTasrif/SH-CLONER > /dev/null 2>&1 && cd SH-CLONER && python sh.py")
