import psycopg2

conn = psycopg2.connect("dbname=Onlinestore user=postgres password=0Ksndjskxw")
cur = conn.cursor()
print("Getting code...")
cur.execute("select profiles.id, sessions.endtime, sessions.duration, sessions.sale, profiles_previously_viewed.prodid, products.category, products.subcategory, products.subsubcategory, products.name, products.targetaudience, products.sellingprice, products.deal from profiles "
            "left JOIN sessions ON profiles.id=sessions.profid "
            "left JOIN profiles_previously_viewed ON profiles.id=profiles_previously_viewed.profid "
            "inner JOIN products ON products.id=profiles_previously_viewed.prodid "
            "ORDER BY profiles.id, sessions.endtime, sessions.sale")

print("Code get!")
print("Reformatting...")
code = cur.fetchall()
profids = []
ids = []
for i in range(100000):
    print("{} van {} formatten...".format(i+1, len(code)))
    current = []
    if code[i][0] not in ids:
        ids.append(code[i][0])
        current.append(code[i][0])
        current.append([[code[i][5], code[i][6], code[i][7], code[i][8]]])
        profids.append(current)
    else:
        for j in range(len(profids)):
            if profids[j][0] == code[i][0]:
                profids[j][1].append([code[i][5], code[i][6], code[i][7], code[i][8]])
                break

uitvoer = 'DataProductsPerUser'

uit = open(uitvoer, 'w')

print("Printing code...")
for i in range(len(profids)):
    print("{} van {} in file...".format(i + 1, len(profids)))
    uit.write(str(profids[i]) + '\n')

uit.close()
print("{} items geprint!".format(len(profids)))

cur.close()
conn.close()