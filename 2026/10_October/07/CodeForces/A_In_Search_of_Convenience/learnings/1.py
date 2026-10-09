# *args and **kwargs

# https://www.w3schools.com/python/python_args_kwargs.asp

def solution(name,age,place):
    print(name)
    print(age)
    print(place)
    return [name,age,place]
    

x=["ganu",19,"Mysore"]
# print(solution(x[0],x[1],x[2]))
print(solution(*x)) # unpacking


