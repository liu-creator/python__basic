'''插入100条数据到数据库(每次插入一条)'''
import pymysql
import string,random


#打开数据库连接
conn=pymysql.connect('localhost','root','123456')
conn.select_db('testdb')
#获取游标
cur=conn.cursor()

#创建user表
cur.execute('drop table if exists user')
sql="""CREATE TABLE IF NOT EXISTS `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `name` varchar(255) NOT NULL,
	  `age` int(11) NOT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""

cur.execute(sql)

#修改前查询所有数据
cur.execute("select * from user;")
print('修改前的数据为：')
for res in cur.fetchall():
      print (res)

print ('*'*40)
#循环插入数据
# words=list(string.ascii_letters)
words=list(string.ascii_letters.lower())
sql="insert into user values(%s,%s,%s)"
for i in range(100):
      random.shuffle(words)#打乱顺序
      cur.execute(sql,(i+1,"".join(words[:5]),random.randint(0,80)))

#插入100条后查询所有数据
cur.execute("select * from user;")
print('修改后的数据为：')
for res in cur.fetchall():
      print (res)
print ('*'*40)

cur.close()
conn.commit()
conn.close()
print('sql执行成功')
print(len(words), words)