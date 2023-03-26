import smtplib
import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('emails_names_laptopIDs.xlsx')
file_loc = "C:/Users/ritvi/OneDrive/Desktop/py_scripts/mass_email_automation/emails_names_laptopIDs.xlsx"
read = pd.read_excel(file_loc, index_col=0, header =0)

user_email = input("Enter your email: ")
user_pass = input("Enter your password: ")

# Set up the SMTP server
server = smtplib.SMTP('Smtp.gmail.com')
server.starttls()
server.login(user_email, user_pass)


# Loop through the rows of the dataframe
for i, row in df.iterrows():
    to_email = row['Email']
    name = row['Name']
    laptop_id = row['Laptop ID']


    # Compose the email message
    message = "Dear {},\n\nYour laptop {} is ready for pickup. Please come to the IT Service Center to claim it.\n\nBest regards,\nService Desk- Global".format(name, laptop_id)

from_email = input('Input the "From" email here')
    # Send the email
server.sendmail(from_email, to_email, message)

server.quit()