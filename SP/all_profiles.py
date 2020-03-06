#https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html
#https://api.mongodb.com/python/current/tutorial.html
#https://www.psycopg.org/docs/usage.html

import psycopg2
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

#db = client['test-database']
db = client.huwebshop

col = db.profiles

profiles = col.find()
#print(products[0])
#print(products[0]['name'])
#for x in products:
#    print(x)

print(db)

conn = psycopg2.connect("dbname=Online_store user=postgres password=0Ksndjskxw")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS all_pro;")

cur.execute("CREATE TABLE all_pro (id serial PRIMARY KEY, "
            "_ID varchar, "
            "buids varchar);")
            # "recommendations varchar, "
            # "previously_recommended varchar);")
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
for i in profiles:
    print(i['recommendations']['viewed_before'] if 'recommendations' in i else None)
    print(i['previously_recommended'] if 'previously_recommended' in i else None)
    cur.execute("INSERT INTO all_pro (_ID, buids, recommendations, previously_recommended) VALUES (%s, %s, %s, %s)",
                (i['_id'],
                 i['buids'] if 'buids' in i else None,
                 i['recommendations']['viewed_before'] if 'recommendations' in i else None,
                 i['previously_recommended'] if 'previously_recommended' in i else None))
#ID, category, brand, gender, sub category, sub sub category, color, name, price
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