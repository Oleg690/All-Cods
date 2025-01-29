import cgi, fromUtils

print('Content-type: text/html\n')

params = cgi.FieldStorage()

user = params.getfirst('user', '0')

sql = f"select * from users where user = '{user}'"
result = fromUtils.sendReq(sql)

print(result)