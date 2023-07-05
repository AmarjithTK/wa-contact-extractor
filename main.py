import csv
import re
import truecallerpy
import json
# Input text

text = input("Enter the whatsapp text required")
# text = "ida, Vishnu, +919605471075 Vishnu, vishnuts😈, Yashwanth, +91 86181 83636, +91 70109 29619, +91 93012 21537, +91 91774 30504, +91 73822 51807, +91 73239 34350, +91 96967 96189, +91 95088 79866, +91 75102 92011, +91 95670 77946, +91 89216 30621, +971 58 161 2397, +91 95159 24186, +91 98477 61029, +91 91880 34617, +91 73562 90030, +91 95670 72833, +91 93349 12154, +91 93045 41342, +91 77364 60241, +91 6282 178 226, +91 90398 80899, +91 78980 01630, +91 98472 09509, +91 90147 79151, +91 85901 84937, +91 85998 86683, +91 80898 71033, +9"
id="a1i0w--gT-vSqFz-ychmTFUX7TjMRdWmq8vDyMZGZTJvu9p_amk_K0JCY6s0a9Za"

# Regular expression to match phone numbers with country code
pattern = re.compile(r"\+\d{1,4}\s\d{5}\s\d{5}")

# Find all phone numbers in the text and remove unnecessary spaces
matches = [re.sub(r'\s+', ' ', match.strip()) for match in pattern.findall(text)]

# print(matches)
# Write phone numbers to a CSV file
with open('numbers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    matches = list(set(matches))
    for match in matches:
        writer.writerow([match])



# Read the CSV file
# with open('numbers.csv', 'r') as file:
#     reader = csv.reader(file)
#     numbers = [row[0] for row in reader]
# with open('numbers.csv', 'r') as file:
#     reader = csv.reader(file)
#     numbers = ','.join([row[0].replace(' ', '') for row in reader])
    
# # print(numbers)   


# # output = truecallerpy.search_phonenumber('919605471074','IN',id)
# output = truecallerpy.bulk_search(numbers,"IN", id)

# print(output)

# Send HTTP requests to Truecaller API and store contact names
# contacts = {}
# for number in numbers:
#     owner = truecallerpy.search_phonenumber(number,'IN',id)
#     contacts[number] = json.loads(owner)

# # Write phone numbers and contact names to a new CSV file
# with open('contacts.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Phone Number', 'Contact Name'])
#     for number, name in contacts.items():
#         writer.writerow([number, name])