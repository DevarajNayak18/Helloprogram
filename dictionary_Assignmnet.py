'''
#convert 2 list into dict keys and values
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result={}
for k in keys:
    for v in values:
        result[k]=v
        values.remove(v)
        break
print(result)


#Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)




#3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict["class"]["student"]["marks"]["history"])


#4: Initialize dictionary with default values In Python, we can initialize the keys with the same values.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
x={}.fromkeys(employees,defaults)
print(x)


#5: Create a dictionary by extracting the keys from a given dictionary
#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
new_dict={k:sample_dict[k] for k in keys}
print(new_dict)


#6: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys to remove
keys = ["name", "salary"]
for k in keys:
    #del sample_dict[k]
    sample_dict.pop(k)
#new_dict={k:sample_dict[k] for k in keys}
#del sample_dict[k]

print(sample_dict)
#Expected output:  {'city': 'New york', 'age': 25}


#7: Check if a value exists in a dictionary

#We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

#Write a Python program to check if value 200 exists in the following dictionary.
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 300 in sample_dict.values():
    print("300 value is present in dictionary ")
else:
    print("300 value is not present in dictionary ")

#8: Rename key of a dictionary
#Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}
sample_dict["location"]=sample_dict.pop("city")
print(sample_dict)


#9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75}
z=min(sample_dict)
print(z)


#10: Change value of a key in a nested dictionary
#Write a Python program to change Brad’s salary to 8500 in the following dictionary

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict["emp3"]["salary"]=8500
print(sample_dict)
'''




















































