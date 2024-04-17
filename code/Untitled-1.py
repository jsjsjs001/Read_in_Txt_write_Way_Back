
# Python3 code to demonstrate working of
# Detect date in String
# Using re.search() + strptime()
#https://www.geeksforgeeks.org/python-extract-date-in-string/ 
import aifc
import re
from datetime import datetime
  
# initializing string
#test_str = "gfg at 04-02-2021"
test_str = "gfg at (4. 12. 2015) "
  
# printing original string
print("The original string is : " + str(test_str))
x = test_str.replace(". ", "-")  
#print ("The num string is ", str(test_str).rjust(2, '0'))
print("The replaced string is : " + str(x))
# searching string
a = [r'\d{2}-\d{2}-\d{4}' , r'\d{2}-\d{1}-\d{4}', r'\d{1}-\d{1}-\d{4}', r'\d{1}-\d{2}-\d{4}']
match_str = re.search(r'\d{2}-\d{1}-\d{4}', x)
while a : # and not match_str:
    ai = (a.pop(-1))
    print(ai)
    m_str = re.search(ai, x)
    print(m_str)
    if  m_str: 
        match_str = m_str 
#    match_str = re.search(a, x)

if  match_str:     
    print(match_str)  
    # computed date
    # feeding format
    res = datetime.strptime(match_str.group(), '%d-%m-%Y').date()
    # printing result
    print("Computed date I : "+ str(res))
else: 
    print('ni našel')    


