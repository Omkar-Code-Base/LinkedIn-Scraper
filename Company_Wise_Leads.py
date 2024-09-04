import requests
import re
import csv
import os
from urllib.parse import quote

# Script Configuration
print("Company Wise Leads")
print("Please enter your linkedin login credentials")
linkedin_email = input("Enter your LinkedIn login email: ") # place your linkedin login email
linkedin_password = input("Enter your LinkedIn login password: ") # place your linkedin login password
target_company_link = "https://www.linkedin.com/company/" + input("Enter company name :") +"/" # place company URL in mentioned format only! do not remove trailing slash
# End Script Configuration

class LinkedIn:
    def __init__(self):
        self.s = requests.Session()


if __name__ == "__main__":
    linkedin = LinkedIn()
    if linkedin.login(linkedin_email,linkedin_password):
        print("Logged in successfully")
    else:
        print("Failed to login")