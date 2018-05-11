from crate import client
import MySQLdb
import time

connection = client.connect("http://127.0.0.1:4200",username='crate', error_trace=True)
crate = connection.cursor()


start = time.time()
###
crate.execute("SELECT COUNT(*) as count from (SELECT * FROM tweets) as t")
###
done = time.time()
elapsed = done - start
print("CRATE: "+str(elapsed))

result = crate.fetchall()
#print(result)



connection2 = MySQLdb.connect(host="127.0.0.1",    # your host, usually localhost
                     user="root",         # your username
                     passwd="passwordtest",
                     database="sakila")
mysql = connection2.cursor()

start = time.time()
###
mysql.execute("SELECT COUNT(*) as 'count' from ( SELECT * FROM tweets ) as t")
###
done = time.time()
elapsed = done - start
print("MYSQL: "+str(elapsed))

result = mysql.fetchall()
#print(result)
