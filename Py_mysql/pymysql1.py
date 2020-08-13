import pymysql


#打开数据库连接
conn = pymysql.connect('localhost',port=3306,user = "root",passwd = "123456",db = "testdb")
#获取游标
cursor=conn.cursor()
print(cursor)

#创建user表
cursor.execute('drop table if exists user')
sql="""CREATE TABLE IF NOT EXISTS `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `name` varchar(255) NOT NULL,
	  `age` int(11) NOT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

cursor.execute(sql)
cursor.close()#先关闭游标
conn.close()#再关闭数据库连接
print('创建数据表成功')


'''插入单条数据'''

#打开数据库连接，不指定数据库
conn=pymysql.connect('localhost','root','123456')
conn.select_db('testdb')

cur=conn.cursor()#获取游标

#创建user表
cur.execute('drop table if exists user')
sql="""CREATE TABLE IF NOT EXISTS `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `name` varchar(255) NOT NULL,
	  `age` int(11) NOT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

cur.execute(sql)

insert=cur.execute("insert into user values(1,'tom',18)")
print('添加语句受影响的行数：',insert)

#另一种插入数据的方式，通过字符串传入值
sql="insert into user values(%s,%s,%s)"
cur.execute(sql,(3,'kongsh',20))

cur.close()
conn.commit()
conn.close()
print('sql执行成功')



'''插入多条数据'''
#打开数据库连接，不指定数据库
conn=pymysql.connect('localhost','root','123456')
conn.select_db('testdb')
#获取游标
cur=conn.cursor()

#另一种插入数据的方式，通过字符串传入值
sql="insert into user values(%s,%s,%s)"
insert=cur.executemany(sql,[(4,'wen',20),(5,'tom',10),(6,'test',30)])
print ('批量插入返回受影响的行数：',insert)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')

#打开数据库连接
conn= pymysql.connect('localhost','root','123456')
conn.select_db('testdb')
#获取游标
cur=conn.cursor()

cur.execute("select * from user;")
while 1:
    res=cur.fetchone()
    if res is None:
        #表示已经取完结果集
        break
    print (res)
cur.close()
conn.commit()
conn.close()
print('sql执行成功')



'''更新单条数据'''
#打开数据库连接
conn=pymysql.connect('localhost','root','123456')
conn.select_db('testdb')
#获取游标
cur=conn.cursor()

#更新一条数据
update=cur.execute("update user set age=100 where name='kongsh'")
print ('修改后受影响的行数为：',update)
#查询一条数据
cur.execute('select * from user where name="kongsh";')
print(cur.fetchone())
cur.close()
conn.commit()
conn.close()
print('sql执行成功')


