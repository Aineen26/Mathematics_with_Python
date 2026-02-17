def Armstrong_No(num,sum=0):
    temp=num
    while num>0:
        rem = num % 10
        sum = sum + rem**3
        num = num//10
    if temp==sum:
        print("Given number is Armstrong")
    else:
        print("Given number is not Armstrong")

Armstrong_No(num=int(input("Enter a number: ")))