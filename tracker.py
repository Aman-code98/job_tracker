import os #importing the os module to check if the file exists on my laptop
import json # importing the json module to read and write json files

Valid_status = ['applied', 'interviewing', 'offer', 'rejected']

# Check if the the Jobs file exists else create a new list to store job applications
if os.path.exists('jobs.json'):
    with open('jobs.json', 'r') as file:
        jobs = json.load(file)
else:
    jobs = []

# Get user input for the job application details and append the new job application to the Empty jobs listz
company = input("Enter the company name: ").strip()
while company == "":
    print("Company name cannot be empty. Please enter a valid company name.")
    company = input("Enter the company name: ").strip()
title = input("Enter the job title: ").strip()
while title == "":
    print("Job title cannot be empty. Please enter a valid job title.")
    title = input("Enter the job title: ").strip()
status = input("Enter the job status (applied, interviewing, offer, rejected): ").strip().lower()
while status not in Valid_status:
    print("Invalid status. Please enter a valid status.")
    status = input("Enter the job status (applied, interviewing, offer, rejected): ").strip().lower()

jobs.append({
    "company": company,
    "title": title,
    "status": status
})

# Save the updated jobs list to the jobs.json file and print the number of jobs saved.
with open('jobs.json', 'w') as file:
    json.dump(jobs, file)

print('jobs saved', len(jobs))

print("List of job applications:")
for index, job in enumerate(jobs, start = 1):
    print(f"{index}. {job['company']} - {job['title']} ({job['status']})")

