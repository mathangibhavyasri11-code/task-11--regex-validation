# Q2. Import the re module and understand pattern matching.
import re
# Q3. Write a regex pattern to validate email addresses.
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)
# Q4. Create pattern to validate Indian mobile numbers.
def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, mobile)
# Q5. Add password validation logic (length, digit, special character).
def validate_password(password):
    pattern = r'^(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{8,}$'
    return re.match(pattern, password)
# Q6. Accept user input dynamically and validate.
email = input("Enter Email: ")
mobile = input("Enter Mobile Number: ")
password = input("Enter Password: ")
# Q7. Display meaningful validation messages.
if not email:
    print("Email cannot be empty.")
elif validate_email(email):
    print("Valid Email.")
else:
    print("Invalid Email format.")
if not mobile:
    print("Mobile number cannot be empty.")
elif validate_mobile(mobile):
    print("Valid Indian Mobile Number.")
else:
    print("Invalid Mobile Number.")
if not password:
    print("Password cannot be empty.")
elif validate_password(password):
    print("Strong Password.")
else:
    print("Password must be at least 8 characters long, include a digit and a special character.")
# Q8. Organize regex logic into reusable functions.
# Email, mobile, and password validations are separated into functions.