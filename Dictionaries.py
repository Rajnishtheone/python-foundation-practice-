

student={
    "raj":12,
    "mohit":52,
    "mob":99999,
    0:100.0,
    "age":10
}

print(student["mob"])

print(student.get("bib",9))

#Adding and Updating

student["country"]="india"

student ["age"]=20

print(student)



# Removing dictionary items

# Method	        Purpose

# pop()         	Removes a specified key
# popitem()     	Removes the last inserted pair
# del	            Deletes a specified key
# clear()	        Removes everything

print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
    print(key ,":= ", " ", value)

    child={
        "child1":{
            "name":"rajnish",
            "age":24,
            "class":2
        },
        "child2":{
            "name":"munna",
            "age":10,
            "class":3
        }
    }

    print(child["child2"]["age"])


# List vs Tuple vs Set vs Dictionary
# Feature	List	Tuple	Set	Dictionary
# Syntax	[]	()	{}	{key:value}
# Ordered	Yes	Yes	No guaranteed order	Yes
# Duplicates	Yes	Yes	No	Keys: No
# Changeable	Yes	No	Yes	Yes
# Access	Index	Index	No index	Key