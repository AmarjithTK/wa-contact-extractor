import re
import csv

# Read the HTML file
with open('file.html', 'r') as file:
    html = file.read()

# Regex pattern to match a specific pattern in the HTML
pattern = r"\+\d{1,4}\s\d{5}\s\d{5}"

# Find all matches of the pattern in the HTML
matches = re.findall(pattern, html, re.DOTALL)


with open('numbers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    matches = list(set(matches))
    for match in matches:
        writer.writerow([match])
# Print the extracted matches
# for match in matches:
#     print(match)
