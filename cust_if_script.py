#!/usr/bin/env python3
"""My Custom IF, Budget
   Lucy Chen | lchen6695@gmail.com"""

message = 'Your budget is 1000k, ' 

spending  = float(input("How much are you spending?"))

if spending >= 1001:
    message = message + 'you are over your budget. You are in debt.'

elif spending == 1000:
    message = message + 'you have reached the end of your budget. Better luck next time.'

elif spending == 500:
    message = message + 'you have half your budget left.'

elif spending <= 800:
    message = message + 'keep on spending.'

elif spending >= 800:
    message = message + 'you are close, stop spending!'

else: 
    message = message + 'still the same.'

print(message)
