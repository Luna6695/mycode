#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginsuccess = 0 # counter for successful logins

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
         print(line.split("172.16.1.5")[-1])
