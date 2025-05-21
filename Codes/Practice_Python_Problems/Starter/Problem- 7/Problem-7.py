def fizznumber(number):
    if number%3==0 and number%5==0:
        return "Fizzbuzz"
    elif number%3==0:
        return "Fizz"
    elif number%5==0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"
    
print(fizznumber(3))
print(fizznumber(15))
print(fizznumber(5))
print(fizznumber(37))
print(fizznumber(40))