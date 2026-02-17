def lowercase(str,upper=0,lower=0):
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            pass
    print(f"Uppercase count: {upper}")
    print(f"Lowercase count: {lower}")

lowercase(str = input("Enter a string: "))