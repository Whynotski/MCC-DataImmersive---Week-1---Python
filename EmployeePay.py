
# Laura Adam 4/8/2019

#Employee Pay
#write a program that calculates the salary for the week of the employees listed below.
#If an employee worked more than 40 hours that week, then
#   calculate the remaining hours as time and a half (1.5x the normal rate).
# The program should print their name and salary earned.


name=input("Enter Employee Name:  ")

hours=input("Enter Hours worked:")
int(hours)
rate=input("Enter Hourly Rate:")
int(rate)
if int(hours) <= 40:
  pay = int(hours) * int(rate)
else:
  pay = int(hours) * int(rate) * 1.5
int(pay)
print("Name: ", name, "your earned salary is $", pay)


