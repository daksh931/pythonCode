name = input("Enter your Name : ")
dept = input("Enter your Department : ")
sal = int(input('Enter your Salary : '))

if sal<10000 :
    HRA = 1500
    DA = 800
    TA = 500
    Tax = 0.125*sal
    NetSal = sal-(0.125*sal)
    print('Name : ',name , '\nDepartment : ',dept ,'\nHRA' , HRA , '\nDA : ', DA , '\nTA : ',TA , '\n Tax' , Tax , '\n Net Salary : ' ,NetSal)


elif 10001 <sal< 20000 :
    HRA = 2200
    DA = 1500
    TA = 1100
    Tax = 0.125*sal
    NetSal = sal-(0.125*sal)
    print('Name : ',name , '\nDepartment : ',dept ,'\nHRA' , HRA , '\nDA : ', DA , '\nTA : ',TA , '\n Tax' , Tax , '\n Net Salary : ' ,NetSal)

if 20000<sal :
    HRA = 3000
    DA = 2000
    TA = 1600
    Tax = 0.125*sal
    NetSal = sal-(0.125*sal)
    print('Name : ',name , '\nDepartment : ',dept ,'\nHRA' , HRA , '\nDA : ', DA , '\nTA : ',TA , '\n Tax' , Tax , '\n Net Salary : ' ,NetSal)