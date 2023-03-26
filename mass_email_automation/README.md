The purpose of this script is to  automate the process of mass emailing while still personalizing each email.

# Example Use Case

Suppose a group of 40 people were recently hired at a company and a team member from the IT Service Desk/ Help Desk needs to send out an email to the group informing them to pick up a corporate laptop.
 
This script reads an Excel sheet of employee names and associated laptop numbers (as assigned by the company) and write each employee an email that the laptop is read for pick up.

# Script Inputs

This script takes 2 inputs.

1. Email credentials supplied by user. (These values is not hard- coded for security purposes)
  a. Note: This script uses public Gmail SMTP servers to send the automated emails. Minor changes would be required if private/ corporate email servers are in use. 
2. file path of the employee names and laptop numbers assigned by the company.
