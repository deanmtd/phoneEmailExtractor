#This script Extracts email addresses and phone numbers from a CSV file, saving them to separate CSV files.

import csv
import re

#Replace "PATH_Dir" with the relevant file path and file names:
input_file = r"PATH_Dir\emailAddsNumbers.csv"
email_output_file = r"PATH_Dir\emailAddresses.csv"
phone_output_file = r"PATH_Dir\phoneNumbers.csv"

email_addresses = []
phone_numbers = []

try:
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader:
            email, phone = row
            email_addresses.append(email)
            phone_numbers.append(phone)

    # Write email addresses to emailAddresses.csv
    with open(email_output_file, 'w', newline='') as email_file:
        writer = csv.writer(email_file)
        writer.writerow(['Email'])  # Header row
        for email in email_addresses:
            writer.writerow([email])

    # Extract names from email addresses
    names = []
    for email in email_addresses:
        name_match = re.search(r'([^@]+)@', email)
        if name_match:
            names.append(name_match.group(1))
        else:
            names.append("unknown")

    # Write phone numbers to phoneNumbers.csv with corresponding names
    with open(phone_output_file, 'w', newline='') as phone_file:
        writer = csv.writer(phone_file)
        writer.writerow(['Name', 'Phone Number'])  # Header row
        for name, phone in zip(names, phone_numbers):
            writer.writerow([name, phone])

    print(f"Email addresses saved to {email_output_file}")
    print(f"Phone numbers saved to {phone_output_file}")

except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")