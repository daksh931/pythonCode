a = input('Enter Name of Your Vehicle - ')
b = int(input('Enter Distance Covered by Your Vehicle in Km - '))
c = int(input('Enter Fuel used in Litres - '))

avg = b/c;
print ('Average Of Your Vehicle is - ', avg,' kmpl')

print ('Fuel Efficiency is ',avg ,'km')

if avg>24:
    print('Your Vehicle have Exellence Average')

elif 18<avg<23:
    print('Your Vehicle have Moderate Average')

else :
    print('Your vehicle have Poor Average')