'''删除单条数据'''
import pymysql


#打开数据库连接
conn=pymysql.connect('localhost','root','123456')
conn.select_db('testdb')
#获取游标
cur=conn.cursor()

#删除前查询所有数据
cur.execute("select * from user;")
print('删除前的数据为：')
for res in cur.fetchall():
      print (res)

print ('*'*40)
#删除1条数据
cur.execute("delete from user where id=1")

#删除后查询所有数据
cur.execute("select * from user;")
print('删除后的数据为：')
for res in cur.fetchall():
      print (res)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')
