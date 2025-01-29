import cgi
import dbUtils

params = cgi.FieldStorage()

name = params.getfirst('name', '0')
price = params.getfirst('price', '0')

sql = f"insert into groceries (name, price) values('{name}', {int(price)})"

dbUtils.execSql(sql)