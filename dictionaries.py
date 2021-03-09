# Sort dictionary by keys and values

my_directory = {"first name" : "Rehan", "last name" : "Aziz", "age" : 27}
users_directory = [{"first name" : "Rehan", "last name" : "Aziz", "age" : 27},
                   {"first name" : "Adnan", "last name" : "Aziz", "age" : 28}
                   ] 

# Sort dictionary by keys 
print(sorted(my_directory.keys()))


# Sort dictionary by values 
print(sorted(my_directory.values()))

# Sort list of disctionaries by value
print sorted(users_directory, key = lambda i: i['first name'])
