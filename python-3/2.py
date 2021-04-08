def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("The example of recursion")
tri_recursion(6)
print("2017112181 김만철")