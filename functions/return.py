def add(a,b):
    return a+b

result = add(10,30)

print(result)

#default parameters

#if we don't provide an argument, Python uses "Guest"

def greet(name="guest"):
    print("hello",name)

greet()
greet("rajnish")

# keyWord arguments

def nam(name,age):
    print("hello my name is ",name ,"my age is ",age)

nam("rajnish",20)

def add_num(*numbers):
    total=0
    for num in numbers:
        total = total+num

    return total       

print(add_num(10,20))



ans=add_num(10,10,30,40)
print("ans = ",ans)

# Variable-length keyword arguments: **kwargs

def details(**det):
    print(det)


details(name="rajnish",clas="12",city="delhi")    

#lamda function

def mul(x):
    return x*x

print(mul(3))

#lamda version

addd = lambda a,b :a+b

print(addd(5,5))