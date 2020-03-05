from pymongo import MongoClient
import psycopg2
client = MongoClient('localhost', 27017)

#db = client['test-database']
db = client.huwebshop

col = db.products

products = col.find()
#print(products[0])
#print(products[0]['name'])
#for x in products:
#    print(x)


conn = psycopg2.connect("dbname=Online_store user=postgres password=wachtwoord")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS products;")

cur.execute("CREATE TABLE products (id varchar PRIMARY KEY, brand varchar, category varchar, sub_category varchar,"
            " sub_sub_category varchar, gender varchar, color varchar, name varchar, price float);")
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
for i in products:
    cur.execute("INSERT INTO products (id, brand, category, sub_category, sub_sub_category, gender,"
                " color, name, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (i['_id'],
                 i['brand'] if 'brand' in i else None,
                 i['category'] if 'category' in i else None,
                 i['sub_category'] if 'sub_category' in i else None,
                 i['sub_sub_category'] if 'sub_sub_category' in i else None,
                 i['gender'] if 'gender' in i else None,
                 i['color'] if 'color' in i else None,
                 i['name'] if 'name' in i else None,
                 (i['price']['selling_price'])/100 if 'price' in i else None))
"""
# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")
"""
# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()