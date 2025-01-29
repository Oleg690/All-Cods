import datetime

print(
    '''
<!DOCTYPE html>
<html>
<head>
    <title>Date and Time</title>
</head>
<body>
    <p>Current time:</p>
    '''
)

x = datetime.datetime.now().time()

print(
    '<p><b>' + str(x) + '''
</b></p>
</body>
</html>
'''
)