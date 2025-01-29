import cgi
import dbUtils

params = cgi.FieldStorage()

id_ = params.getfirst('id', '0')

sql = f"delete from groceries where id = {int(id_)}"

dbUtils.execSql(sql)