# Phyllis Torres
# 16.7 Date Calculations Assignment
# Due 11/10/2016

# import date and time from datetime module
from datetime import datetime

print('16.7 Age and Time Remaining until Next Birthday Calculations Assignment\n')
print('Phyllis Torres\n\n')

print("This program will prompt the user for a birthdate, calculate the user's age, and calculate the time remaining until the user's next birthday.")

# define function to calculate a person's age using a user input birthdate
def calculate_age():
    if cdate > datetime(cdate.year, bdate.month, bdate.day):
        age = cdate.year - bdate.year
        next_year = True
    else:
        age = cdate.year - bdate.year - 1
        next_year = False
    print("\nYou are {} years old.".format(age))
    return next_year

# define function to calculate the time to the user's next birthday
def time_2next_birthday():
    time2bday = datetime(cdate.year + next_year, bdate.month, bdate.day) - cdate
    days = time2bday.days
    hours, remainder = divmod(time2bday.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    print ('\nYou have ' + str(days) + ' days,'),
    print (str(hours) + ' hours,'),
    print (str(minutes) + ' minutes, and'),
    print (str(seconds) + ' seconds'),
    print ('left until your next birthday!!!')

# prompt user to enter their birthdate in mm/dd/yyyy format
bdateInput = input('\nPlease enter the date of your birth in the format "mm/dd/yyyy" and include quote marks: ')

# format bdate from input
bdate = datetime.strptime(bdateInput, '%m/%d/%Y')

# get the current date
cdate = datetime.now()

# call function to calculate age
next_year = calculate_age()

# call function to calculate time to next birthday
time_2next_birthday()
