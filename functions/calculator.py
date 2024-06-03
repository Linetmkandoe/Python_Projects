# def add(x,y):
#     """adding"""
#     result = x+y
#     return result
# def subtract(a,b):
#     """subtracting"""
#     result = a-b
#     return result
# def divide(a,b):
#     """dividing"""
#     result = a/b
#     return result

# def simple_interest(p,t,r):
#     """intrest"""
#     print('The principal is',p)
#     print('The time period is',t)
#     print('The rate of interest is',r)

#     si =(p*t*r)/100
#     print('The simple interest is', si)
#     return si

# simple_interest(10,40,20)

# def reverse_String(string):
#     """reversing"""
#     # x="Linet"
#     reversed= string.lower()
#     reversed_string=reversed[::-1]
   
#     # return reversed[::-1]mytxt=reverse_String(str)
# print(reverse_String("Linet"))

def sum(*numbers):
    """sum"""
    total=0
    for number in numbers:
        total +=total
    return total
def mutiply_many(*numbers):
    """mutiply"""
    mutiply=1
    for number in numbers:
        mutiply*=mutiply
    return mutiply



