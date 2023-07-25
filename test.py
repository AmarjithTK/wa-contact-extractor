import phonenumbers

# Text input
text = input("Enter text")

# Pass the text and country code to the PhoneNumberMatcher
numbers = phonenumbers.PhoneNumberMatcher(text, "IN")

# Printing the phone numbers matched with country code
# and also the indexes of the phone numbers in the string input
for number in numbers:
    phone_number = phonenumbers.format_number(number.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    print(phone_number)





    