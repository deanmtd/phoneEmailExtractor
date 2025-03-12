# Email and Phone Number Extractor

This Python script extracts email addresses and phone numbers from a CSV file and saves them into separate CSV files.

## Purpose

The script reads a CSV file containing email addresses and phone numbers, extracts the email addresses and phone numbers, and then writes them to two separate CSV files. The names associated with each phone number are extracted from the email address.

## Files

* `emailAddsNumbers.csv`: (Input) A CSV file containing email addresses and phone numbers in two columns: "Email" and "Phone Number".
* `emailAddresses.csv`: (Output) A CSV file containing the extracted email addresses in a single column: "Email".
* `phoneNumbers.csv`: (Output) A CSV file containing the extracted phone numbers and corresponding names (extracted from the email addresses) in two columns: "Name" and "Phone Number".

## Prerequisites

* Python 3.x installed.

## How to Use

1.  **Prepare the Input File:**
    * Create a CSV file named `emailAddsNumbers.csv` in the `Data` directory, or ensure that the file exists at the specified path.
    * The file should have two columns: "Email" and "Phone Number".
    * Example:

    ```csv
    Email,Phone Number
    john.doe@example.com,+27 12 345 6789
    jane.smith@example.com,+27 21 987 6543
    ```

2.  **Run the Script:**
    * Open a terminal or command prompt.
    * Navigate to the directory containing the Python script.
    * Run the script using the following command:

    ```bash
    python your_script_name.py
    ```
    * Replace `your_script_name.py` with the actual name of your Python script.
	
### Code:

```python
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
```

3.  **Check the Output Files:**
    * The script will create two CSV files: `emailAddresses.csv` and `phoneNumbers.csv` in the same directory as the input file, or the directories specified in the script.
    * Open these files to verify the extracted email addresses and phone numbers.

## Script Details

The script performs the following steps:

1.  Reads the input CSV file.
2.  Extracts email addresses and phone numbers.
3.  Writes email addresses to `emailAddresses.csv`.
4.  Extracts names from email addresses.
5.  Writes phone numbers and corresponding names to `phoneNumbers.csv`.
6.  Handles potential `FileNotFoundError` exceptions.

## Modifications

* To change the input and output file paths, modify the following variables at the beginning of the script:

    ```python
    input_file = r"C:\Users\Dean\Documents\pyScripts\emailPhoneExtractor\Data\emailAddsNumbers.csv"
    email_output_file = r"C:\Users\Dean\Documents\pyScripts\emailPhoneExtractor\Data\emailAddresses.csv"
    phone_output_file = r"C:\Users\Dean\Documents\pyScripts\emailPhoneExtractor\Data\phoneNumbers.csv"
    ```

* To modify the name extraction logic, change the regular expression used in the following line:

    ```python
    name_match = re.search(r'([^@]+)@', email)
    ```
