from validate_email import validate_email

emailIsValid = validate_email('', verify=True)

if emailIsValid:
    print('True')
else:
    print('False')