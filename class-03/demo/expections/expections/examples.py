x = input('Enter an integer: ')

try:
    z = 3/'hi'
    y = 10/int(x)
except ZeroDivisionError:
    print("you can't divide by zero")
except TypeError as e:
    print(f'Type error happened: {e}')
else:
    print(y)
finally:
    print('Thanks, see you later!')



# x = 2/'5'
# For developers
# age = input("how old are you? ")
# if int(age)<0:
#     raise ValueError("Age should be a positive number.")

try:
    age = input("how old are you? ")
    if int(age)<0:
        raise ValueError("Age should be a positive number.")
    print('after exception')
except ValueError as e:
    print(e)
