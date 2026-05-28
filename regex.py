import re
# 1. Email Validation
email = "test123@gmail.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
# 2. Mobile Number Validation
mobile = "9876543210"
mobile_pattern = r'^[6-9]\d{9}$'

if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
# 3. Name Validation
name = "Ruchika Saini"
name_pattern = r'^[A-Za-z ]+$'

if re.match(name_pattern, name):
    print("Valid Name")
else:
    print("Invalid Name")
# 4. Password Validation
password = "Abc@1234"
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'

if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

# 5. PAN Card Validation
pan = "ABCDE1234F"
pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

if re.match(pan_pattern, pan):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")

# 6. Aadhaar Validation
aadhaar = "123456789012"
aadhaar_pattern = r'^\d{12}$'

if re.match(aadhaar_pattern, aadhaar):
    print("Valid Aadhaar Number")
else:
    print("Invalid Aadhaar Number")
# 7. Extract Numbers from String
text = "My marks are 85 and 90"

numbers = re.findall(r'\d+', text)

print("Numbers Found:", numbers)
# 8. Extract Emails from Text
text2 = "Contact us at support@gmail.com and admin@yahoo.com"

emails = re.findall(
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    text2
)

print("Emails Found:", emails)

# 9. Date Validation
date = "28-05-2026"
date_pattern = r'^\d{2}-\d{2}-\d{4}$'

if re.match(date_pattern, date):
    print("Valid Date Format")
else:
    print("Invalid Date Format")

# 10. URL Validation
url = "https://google.com"
url_pattern = r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

if re.match(url_pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")

# 11. Remove Numbers using re.sub()
sample = "Python123"

result = re.sub(r'\d', '', sample)

print("After Removing Numbers:", result)