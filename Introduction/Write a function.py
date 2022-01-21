# Author: Thomas George Thomas
# Language: python3
def is_leap(year):
    leap = False
    
    # Write your logic here
 
    return (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0)

