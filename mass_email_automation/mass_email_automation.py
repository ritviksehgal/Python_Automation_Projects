import smtplib
import pandas as pd

# Read the data from the Excel file
df = pd.read_excel('emails_names_laptopIDs.xlsx')
file_loc = "C:/Users/ritvi/OneDrive/Documents/Desktop/py_scripts/mass_email_automation/emails_names_laptopIDs.xlsx"
read = pd.read_excel(file_loc, header =0)

user_email = input("Enter your email: ")
user_pass = input("Enter your application- specific password: ")  # create an app- specific password at https://myaccount.google.com/apppasswords

# Set up the SMTP server
server = smtplib.SMTP('Smtp.gmail.com')
server.starttls()
server.login(user_email, user_pass)


# Loop through the rows of the dataframe
for i, row in df.iterrows():
    to_email = row['Email']
    name = row['Name']
    laptop_id = row['Laptop ID']
    #cc_email = input('Input the "CC" email here (optional):')

    # Compose the email message
    subject = 'Your Laptop is Ready for Pickup!'
    message =f"Subject: {subject}\n\n Dear {name},\n\nYour laptop {laptop_id} is ready for pickup. Please come to the IT Service Center to claim it.\n\nBest regards,\nService Desk- Global".format(name, laptop_id)
    from_email = user_email
    server.sendmail(from_email, to_email, message)

server.quit()
