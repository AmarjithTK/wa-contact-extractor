import re
import phonenumbers
from bs4 import BeautifulSoup

# Read the HTML file
with open('file.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all text in the HTML
text = soup.get_text()

# Regular expression pattern for matching phone numbers
pattern = r"\+?\d*[\( -]?\d{3}[\) -]?\d{3}[ -]?\d{2}[ -]?\d{2}"

# Find all phone number matches in the text
matches = re.findall(pattern, text)

# List to store the formatted phone numbers
formatted_numbers = []

# Iterate over the matches and format the phone numbers using phonenumbers library
for match in matches:
    parsed_number = phonenumbers.parse(match, "IN")  # Replace "IN" with the appropriate country code
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_numbers.append(formatted_number)

# Print the formatted phone numbers
print(formatted_numbers)
