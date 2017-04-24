import MySQLdb as mdb


db = mdb.connect('localhost', 'michael', 'mikeman', 'twitterbot')
cursor = db.cursor()

# cursor.execute('DROP TABLE IF EXISTS USERS')

sql = """INSERT INTO USERS(
         USERNAME, PASSWORD, EMAIL)
         VALUES('Luke', 'lukeywarm', 'luke@luke.com')"""

# sql = """DELETE FROM USERS WHERE EMAIL = "mswartz91095@gmail.com" """


try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()


db.close
