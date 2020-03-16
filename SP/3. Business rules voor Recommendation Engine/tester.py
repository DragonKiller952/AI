import psycopg2

conn = psycopg2.connect("dbname=Online_store user=postgres password=0Ksndjskxw")
cur = conn.cursor()
cur.execute("select * from products")
code = cur.fetchall()
print(code)

cur.close()
conn.close()