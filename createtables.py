import MySQLdb as mdb


db = mdb.connect('localhost', 'michael', 'mikeman', 'twitterbot')
cursor = db.cursor()

# cursor.execute('DROP TABLE IF EXISTS USERS')

sql = """CREATE TABLE USERS (
         ID INT PRIMARY KEY AUTO_INCREMENT,
         USERNAME CHAR(20) NOT NULL,
         PASSWORD CHAR(20) NOT NULL,
         EMAIL char(50) NOT NULL)"""

cursor.execute(sql)

db.close
