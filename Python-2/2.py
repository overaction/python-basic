fruitlist = ["banana", "Orange", "Kiwi", "cherry"]
print('Original list : ', fruitlist)

fruitlist.reverse()
print('reverse() -> list ', fruitlist)

fruitlist.sort()
print('sort() -> list ', fruitlist)

fruitlist.sort(key=str.lower)
print("sort(key=str.lower) -> ",fruitlist)

print('2017112181 김만철')
