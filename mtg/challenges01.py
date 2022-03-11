#!/usr/bin/env python3 
"""Trying to write my own API code

    Description:
    A script to interact with an "open" api,
    https://api.nasa.gov/"""

# imports goes on top 
import requests

# define our "base" API
API = "https://api.nasa.gov/" # will never chage regardless of lookup we perform

def main():
    """Run time code"""

    resp = requests.get(f"{API}sets")

    print( resp.json().keys() )
    
if __name__ == "__main__":
    main()
