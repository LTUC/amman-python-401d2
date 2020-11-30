# Red Green Refactor

def fizz_buzz(num):
    # if num is not an integer
    if type(num) != int:
        return 'Invalid Input'
    if num%3 == 0 and num%5 == 0:
        return 'FizzBuzz'
    if num%3 == 0:
        return 'Fizz'
    if num%5 == 0:
        return 'Buzz'
    else:
        return num
