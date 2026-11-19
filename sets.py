# set is collection of unique items // it automatically removes the duplicate values

items = {10,20,30,10,10,10,10, "saachin","raj","raj"}

print(items)

# to create aempty set

items = set()

# this creates empty dictionary

items = {}

# these is no append , insert , it has add, remove, pop , clear, update, discard

# Operation	         Meaning	         Symbol
# Union	      Everything from both sets      |
# Intersection	Common items	               &
# Difference	Items only in first set	          -
# Symmetric difference	Items not common	  ^


# issubset() checks whether all items of one set exist in another.



# issuperset() checks whether one set contains all items of another.



# isdisjoint() checks whether two sets have no common items.

emails=[
    "rajnish@gmail.com",
    "asjgfkas@gmail.com",
    "rajnish@gmail.com",
    "rajn445sh@gmail.com",
    "rajnish@gmail.com",
    "rajn44@gmail.com",
    "rajn44@gmail.com",
]

uniq_email = set(emails)

print(uniq_email)
