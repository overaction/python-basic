def myfunc(n):
    return lambda a: a*n


mydoubler = myfunc(2)
print(mydoubler(5))

mytripler = myfunc(3)
print(mytripler(5))

print('2017112181 김만철')