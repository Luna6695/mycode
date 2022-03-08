#!/usr/bin/env python3
"""A simple script to move two files into ceph/storage/
   Lucy Chen  | lchen6695@gmail.com"""

# Standard library imports
import shutil # shell utilities will be used to move files 
import os # provides access to low level os operation (agnostic to flavor of Os)

def main():
    """called at runtime"""
    os.chdir('/home/student/mycode/') # move into this working directory
    shutil.move('raynor.obj', 'ceph_storage/' # try moving the file raynor.obj into this ceph_storage/ dir

    # program will pause while we accept input 
    xname = input('What is the new name for kerrigan.obj?') # collecct string input from the user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  # moving kerrigan.obj into ceph_storage/ with new name 

main() #this calls out main function
