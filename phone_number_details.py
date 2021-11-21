import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Enter Mobile Number With Country Code: ")
mobileNo = phonenumbers.parse(mobileNo)

# Get timezone a phone number
print(timezone.time_zones_for_number(mobileNo))

# Getting carrier of a phone number
print(carrier.name_for_number(mobileNo, "en"))

# Getting region information
print(geocoder.description_for_number(mobileNo, "en"))

# Validating a phone number
print("Valid Mobile Number: ", phonenumbers.is_valid_number(mobileNo))

# Checking possibility of a number
print("Checking possibility of Number: ", phonenumbers.is_possible_number(mobileNo))