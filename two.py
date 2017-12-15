"""
You go on a wonderful holiday leaving on day number 3 (a Wednesday).
You return home after 137 sleeps.
Write a general version of the program which asks
for the starting day number,
and the length of your stay,
`and it will tell you the name of day of the
week you will return on.
"""


def day_num_to_name(num):
    if num == 0:
        return "Sunday"
    elif num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    else:
        return day_num_to_name(int(input("Please enter an integer between 0 and 6:")))#trying out some recurrsion here in case somehow they enter something besides 0-6
        
    
#print(daynumtoname(int(input("Please enter an integer between 0 and 6."))))
leave_day = int(input("What day are you leaving? (0-6)"))
away_days = int(input("How many nights are you gone?"))

day_back = (leave_day + away_days) % 7 #leaving this out for now - remember to put back
print("You will return on a",day_num_to_name(day_back))
