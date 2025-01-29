import cgi, fromUtils

print('Content-type: text/html\n')

params = cgi.FieldStorage()

email = params.getfirst('email', '0')

sql = f"select * from users where email = '{email}'"
result = fromUtils.sendReq(sql)

print(result)