a = int(input('Enter First Number : '))
b = int(input('Enter Second Number : '))

print('Choose Operator to perform arithametic operation  (+,-,*,/)')

oper = input('Enter Operator : ')

if oper == '+':
    print('The Sum of numbers is : ' , a+b)

elif oper == '-':
    print('The Difference of numbers is : ' , a-b)

elif oper == '*':
    print('The Product of numbers is : ' , a*b)

elif oper == '/':
    print('The Division of numbers is : ' , a/b)

else :
    print('Enter a Valid Arithamatic operator')
