
# Laura Adam 4/8/2019

#Employee Pay
#write a program that calculates the salary for the week of the employees listed below.
#If an employee worked more than 40 hours that week, then
#   calculate the remaining hours as time and a half (1.5x the normal rate).

# The program should print their name and salary earned.

#First - create a dictionary of key value pairs, where the key is the employee number and
#the value is an array of employee information provided.

#dictionary
employeeList = {'001':['Mary', 15.0, 49],
'002':['John', 22.0, 25],
'003':['Bob', 35.0, 4],
'004':['Mel',43.0, 62],
'005':['Jen', 17.0, 33],
'006':['Sue', 29.0, 45],
'007':['Ken', 40.0, 36],
'008':['Dave',20.0, 17],
'009':['Beth',37.0, 37],
'010':['Ray',16.50, 80]}


#create a for loop to iterate through list

for employeeNum, employeeDetail in employeeList.items():
    #print(employeeDetail)
    
    hour = employeeDetail[2]
    rate = employeeDetail[1]
    
    if hour > 40:
      ot =(hour - 40)*1.5
      pay =(ot +40) * employeeDetail[1]
    else:
      pay = hour * employeeDetail[1]
    print(employeeDetail[0], ", your earned salary this week is $", pay)

   # print("This week's payroll is finished!! ")


 
