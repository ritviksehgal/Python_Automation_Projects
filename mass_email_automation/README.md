The purpose of this script is to  automate the process of mass emailing while still personalizing each email.

# Example Use Case

Suppose a group of 40 people is hired at a company and a team member from the IT Service Desk/ Help Desk needs to send out an email to each member of the group informing them to pick up an assigned corporate laptop.

# Script Inputs

This script takes 2 inputs.

1. Email credentials supplied by user. (This is to authenticate to Gmail STMP servers. Credentials are not hard- coded for security purposes)
  a. Note: This script uses public Gmail SMTP servers to send the automated emails. Minor changes would be required if private/ corporate email servers are in use. 
2. file path of the employee names and laptop numbers assigned by the company.

# Email Output Example

From: (input supplied by user)
To (employee email, read from excel sheet)
CC: (user supplied)

Message:

Dear {name},

Your laptop {laptop ID} is ready for pickup. Please come to the IT Service Center to claim it.

Best regards,
Service Desk- Global
