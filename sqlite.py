import sqlite3

#数据库
conn = sqlite3.connect('cumt_net.db')
c = conn.cursor()
# c.execute('insert into user values(?,?)',('05171723','200711'))
# c.execute('select * from user')
# c.execute('delete from user')
# row = c.fetchone()
# print(row[0])
# print(type(row[0]))

conn.commit()
c.close()
conn.close()