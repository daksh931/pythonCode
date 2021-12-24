a = int(input("Enter a Number"))
sum = 0
while a>0:
    m = a%10
    sum+=m
    a = a/10

print(int(sum))

