def func(*args, **kwargs):
    for x in args:
        print(x)
    print('My name :', kwargs["name"], ' & My Age :', kwargs["age"])


func(1, 2, 3, 4, name='만철', age=24)
print('2017112181 김만철')
