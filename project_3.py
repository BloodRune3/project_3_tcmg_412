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
with open("project_3_output.txt") as file_in:
    array = []
    for line in file_in:
        array.append(line)
        
count = 0

for i in array:
    if i.find("Apr") != -1 and i.find("1995") != -1 and i.find("[11") != -1:
        count += 1
    elif i.find("May") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jun") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jul") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Aug") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Sep") != -1 and i.find("1995") != -1:
        count += 1
        array[count] = i
    elif i.find("Oct") != -1 and i.find("1995") != -1:
        count += 1

countall = len(array)

print("Total Number of Requests in the past six months: ", count)
print("Total Number of Requests: ", countall)

# how many total requests have been made over the entire report, output to txt file


