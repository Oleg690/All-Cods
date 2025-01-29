import cgi
import dbUtils

params = cgi.FieldStorage()

id_ = params.getfirst('id', '1')
name = params.getfirst('name', '0')
price = params.getfirst('price', '0')

sql = f"update groceries set name = '{name}', price = {int(price)} where id = {int(id_)}"

dbUtils.execSql(sql)