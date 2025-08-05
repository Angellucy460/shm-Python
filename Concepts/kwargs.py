## *kwargs -> Key word arguments
## Dictionary{key:value}

# 3 min :try mixing up
def greet(name,nationality):
    print("Name is",name)
    print("From ",nationality)

#KWARGS PROFILE
def employee(**kwargs):
    print(kwargs)

#{key:value}
employee(name="Samson",age=20,degree="Engineering")
employee(name="Samson",country="Kenya",degree="Engineering")