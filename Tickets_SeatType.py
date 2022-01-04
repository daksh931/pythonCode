number_tick = int(input("enter no of tickets - "))
seattype1="Diamond seatType Price = 400"
seattype2="Gold  seatType Price = 300"
seattype3="Silver seatType Price = 200\n"

print(seattype1)
print(seattype2)
print(seattype3)

print('For Diamond enter - 1 \nFor Gold enter    - 2 \n\
For Silver enter  - 3 \n')

a = int(input("Select Your SeatType (Enter Number)- "))

if(a==1):
    total_cost = number_tick*400
    print('Total Cost - ',total_cost)
    
elif(a==2):
    total_cost = number_tick*300
    print('Total Cost - ',total_cost)
    
else :
    total_cost = number_tick*200
    print('Total Cost - ',total_cost)
    



