def findElderBrother(bro1_age, bro2_age):
    if bro1_age > bro2_age:
        return "bro1 is Elder"
    else:
        return "bro2 is Elder"
    
print(findElderBrother(19, 25))
