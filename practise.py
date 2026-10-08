fruits = ['Apple', 'Banana']
fruits.append('Mango')  # .append() adds an item to the end of the list
print(fruits)
print(len(fruits)) # gives you the length of the items in the list.

jobs = [{'company': 'Company A', 'title': 'Job Title A', 'status': 'Status A'}]

# saving the data to the file.
import json
data = ['apple', 'banana']
with open( "fruits.json", "w") as file: 
    json.dump(data, file)


# Reading the data from the json file and loading it into a variable called data.
import json
with open('fruits.json', 'w') as file: # here file is a nickname for 
    data = json.load(file)
    print(data)