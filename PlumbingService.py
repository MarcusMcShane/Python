"""
Program: PlumbingService.py
Author: Marcus McShane 12754943
Last date modified: 27/02/2026
The purpose for this assignment is to calculate the cost for a Plumbing Service Company.
The program is performed by completing 5 tasks,
"""


# Task 1 - Welcome Message

border = ("*#" * 21)
message = ("\n*#*# " + "The Best Cheap Same Day Service." + " *#*#\n" + "*#  " + "Written By McShane, Marcus 12754943" + " *#\n")
welcome_message = border + message + border
print(welcome_message)


print()



# Task 2 - Prompt the user to input number of service hours

number_of_hours = float(input("Enter the number of hours required for the Service: "))
if number_of_hours <= 0:
    print("Error: Please enter a positive number")
else:
    print("Service Hours required: ", number_of_hours)

print()



#Task 3 & 4 - Calculate the total charge for a cleaning service & Display the service cost in Currency format

hourly_charge = 60.00
minimum_charge = 90.00
service_hours = float(input("Enter the number of hours required for the Service: "))
total_charge = hourly_charge * service_hours

if service_hours <= 0:
    print("Error: Please enter a positive number")
elif service_hours < 1.5:
    print("Your total charge for this service is $%0.2f" % minimum_charge)
else:
    print("Your total charge for this service is $%0.2f" % total_charge)

print()



#Task 5 - Input the durations of 6 different jobs and calculations


theSum = 0.0
theCount = 0
theAverage = 0.0
theLongest = 0.0

for jobs in range(0,6):  # Creating a for loop to limit the user to 6 inputs
    job_duration = float(input("Enter the job duration: "))
    
    
    if job_duration >= 1.5:  # Using the if statement to perform calculations based on the condition being true
     theSum += job_duration
     theCount += 1
     theAverage = (theSum / theCount)
     theAverage = round(theAverage, 2)
     
    if job_duration >= 1.5 and job_duration > theLongest:
      theLongest = job_duration

    if job_duration <= 0:
        break # Stopping the loop 

print()

if theCount > 0: #Using theCount variable to verify conditions are met
     print("The count of job durations greater that 1.5 hours: ", theCount)
if job_duration <= 0:
    print("Error: Please re-enter jobs with positive values only")
elif theCount <= 0:
     print("No jobs greater than 1.5 hours")


if theSum > 0:  
    print("The sum of job durations greater that 1.5 hours: ", theSum)

if theAverage > 0:
   print("The average of job durations greater that 1.5 hours: ", theAverage)

   print("The longest of job durations greater that 1.5 hours: ", theLongest)
