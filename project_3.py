# This is our project 3 script that will preform the tasks required in the lab
import requests
from os.path import exists

# Set variables for static values, url, dates etc
url = "https://s3.amazonaws.com/tcmg476/http_access_log"

# check for cached log file or pull the log file from apache server
if not exists("project_3_output.txt"):
    log = requests.get(url)
    with open("project_3_output.txt", 'wb') as out:
        out.write(log.content)
    print("we got the log from the internet")
else:
    print("there was already a log on your local machine")

# how many total requests have been made in the last 6 months, output to txt file


# how many total requests have been made over the entire report, output to txt file

