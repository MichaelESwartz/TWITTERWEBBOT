import MySQLdb as mdb






def logy(u_n, p_s):
    db = mdb.connect('localhost', 'michael', 'mikeman', 'twitterbot')
    cursor = db.cursor()
    sql = "SELECT * FROM USERS WHERE USERNAME = '%s'" % (u_n)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        un = row[1]
        ps = row[2]
        if (ps == p_s ):
            return True
