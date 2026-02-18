def Prime(num,flag = False):
    if num==0 or num==1:
        print(num,"is not a prime number")
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                flag=True
                break
        if flag == 1:
            print(f"{num} is not a prime number")
        else:
            print(f"{num} is a prime number")
    else:
        pass

print(Prime(int(input("Enter a number: "))))