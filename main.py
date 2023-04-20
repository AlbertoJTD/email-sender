import smtplib
from datetime import datetime
import random
import pandas

# Replace content in the letters
PLACEHOLDER_NAME = '[NAME]'
PLACEHOLDER_AUTOR = '[AUTOR]'

# Configuration for your email
autor = "your name here"
email = "your_emaild@gmail.com"
password = "your_key"

# Read CSV file
data = pandas.read_csv('birthdays.csv')

# Get the current date
today = (datetime.now().month, datetime.now().day)

# Check the birthdays.csv file for any birthdays
for index, row in data.iterrows():
    if today[0] == row.month and today[1] == row.day:
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as letter_file:
            letter_content = letter_file.read()
            new_letter = letter_content.replace(PLACEHOLDER_NAME, row['name'])
            birthday_message = new_letter.replace(PLACEHOLDER_AUTOR, autor)

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email,
                                    to_addrs=row.email,
                                    msg=f"Subject:Happy Birthday\n\n{birthday_message}")
