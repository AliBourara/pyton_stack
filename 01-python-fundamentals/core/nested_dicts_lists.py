# 1. Update Values in Dictionaries and Lists

"""
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

x[1][0]=15
print(x)

students[0]["last_name"] = "bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30 
print(z)
"""

# 2. Iterate Through a List of Dictionaries

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]
"""
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""

"""
def iterateDictionary(some_list):
    for list in some_list :
        for key,value in list.items():
            print(f"first_name - {key}, last_name - {value}")

iterateDictionary(students)
"""
# 3. Get Values From a List of Dictionaries
"""
def iterateDictionary2(key_name, some_list):
    for list in some_list :
        for key_name,value in list.items():
            print(value)

iterateDictionary2("first_name", students)
"""

# 4. Iterate Through a Dictionary with List Values

dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": [
        "Michael",
        "Amy",
        "Eduardo",
        "Josh",
        "Graham",
        "Patrick",
        "Minh",
        "Devon",
    ],
}

def printInfo(some_dict):
    for value in some_dict.values():
            for i in value:
                print(i)

printInfo(dojo)