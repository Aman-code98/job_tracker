import os
import json

if os.path.exists('jobs.json'):
    with open('jobs.json', 'r') as file:
        jobs = json.load(file)
else:
    jobs = []

company = input("Enter the company name: ")
title = input("Enter the job title: ")
status = input("Enter the job status (applied, interviewing, offer, rejected): ")

jobs.append({
    "company": company,
    "title": title,
    "status": status
})

with open('jobs.json', 'w') as file:
    json.dump(jobs, file)

print('jobs saved', len(jobs))
