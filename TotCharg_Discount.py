a = input('Enter the name of your product : ')
b = int(input('Enter The Quantity of your product : '))
c = int(input('Enter The Price of your product : '))

d = b*c

if d<5000 :
    print('Discount : ' , d*0.1, '\nTotal Charges : ', d ,'\nNet Price : ' , d-(d*0.1))

elif 5001< d <10000 :
    print('Discount : ' , d*0.15, '\nTotal Charges : ', d ,'\nNet Price : ' , d-(d*0.15))

elif  10000<d :
    print('Discount : ' , d*0.2, '\nTotal Charges : ', d ,'\nNet Price : ' , d-(d*0.2))
