import psycopg2

print("\n### RecommendedPerUser.py ###\n")

conn = psycopg2.connect("dbname=Onlinestore user=postgres password=0Ksndjskxw")
cur = conn.cursor()

print("Setting up tables...")

cur.execute("DROP TABLE IF EXISTS valuesproducts")

cur.execute("CREATE TABLE valuesproducts AS (select id, name, targetaudience, brand, category, subcategory, "
            "subsubcategory, categoryviews, subcategoryviews, subsubcategoryviews, productviews from products)")

cur.execute("DROP TABLE IF EXISTS popular_categorys_per_user")

cur.execute("CREATE TABLE popular_categorys_per_user AS (select id, mostusedcat, mostusedsubcat, mostusedsubsubcat "
            "from profiles)")

cur.execute("ALTER TABLE popular_categorys_per_user ADD catrecommend varchar")
cur.execute("ALTER TABLE popular_categorys_per_user ADD subcatrecommend varchar")
cur.execute("ALTER TABLE popular_categorys_per_user ADD subsubcatrecommend varchar")

conn.commit()

print("Getting data...")

cur.execute("select mostusedcat from popular_categorys_per_user")

categorys = list(set(cur.fetchall()))

cur.execute("select id from valuesproducts where categoryviews is not null and subcategoryviews is not null and"
            " subsubcategoryviews is not null and productviews is not null "
            "order by categoryviews desc,  subcategoryviews desc, subsubcategoryviews desc, productviews desc "
            "limit 1")

defaultcatrec = cur.fetchall()

cur.execute("select mostusedsubcat from popular_categorys_per_user")

subcategorys = list(set(cur.fetchall()))

cur.execute("select id from valuesproducts where subcategoryviews is not null and"
            " subsubcategoryviews is not null and productviews is not null "
            "order by subcategoryviews desc, subsubcategoryviews desc, productviews desc "
            "limit 2")

defaultsubcatrec = cur.fetchall()

cur.execute("select mostusedsubsubcat from popular_categorys_per_user")

subsubcategorys = list(set(cur.fetchall()))

cur.execute("select id from valuesproducts where subsubcategoryviews is not null and productviews is not null "
            "order by subsubcategoryviews desc, productviews desc "
            "limit 3")

defaultsubsubcatrec = cur.fetchall()

print("Calculating category recommendations...")

catrecs = []

for i in range(len(categorys)):
    if categorys[i][0]:
        cur.execute("select id from valuesproducts where categoryviews is not null and "
                    "productviews is not null and category = '{}'"
                    "order by categoryviews desc, subcategoryviews desc, subsubcategoryviews desc, productviews desc "
                    "limit 1".format(categorys[i][0]))
        fetch = cur.fetchall()
        catrecs.append([categorys[i][0], fetch])

for i in range(len(catrecs)):
    if catrecs[i][1]:
        if catrecs[i][0] != 'None':
            name = catrecs[i][0]
            if "'" in name:
                name = name.split("'")
                name = name[0] + "''" + name[1]
                cur.execute("UPDATE popular_categorys_per_user SET catrecommend = '{}' "
                            "WHERE mostusedcat = '{}'".format(catrecs[i][1][0][0], name))
            else:
                cur.execute("UPDATE popular_categorys_per_user SET catrecommend = '{}' "
                            "WHERE mostusedcat = '{}'".format(catrecs[i][1][0][0], name))


cur.execute("UPDATE popular_categorys_per_user SET catrecommend = '{}' "
            "WHERE catrecommend is null".format(defaultcatrec[0][0]))

conn.commit()

print("Calculating subcategory recommendations...")

subcatrecs = []

for i in range(len(subcategorys)):
    if subcategorys[i][0]:
        name = subcategorys[i][0]
        if "'" in name:
            name = name.split("'")
            name = name[0] + "''" + name[1]
            cur.execute("select id from valuesproducts where subcategoryviews is not null and productviews is not null "
                        "and subcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, subsubcategoryviews desc, "
                        "productviews desc "
                        "limit 2".format(name))
            fetch = cur.fetchall()
            if len(fetch) == 1:
                subcatrecs.append([name, [fetch[0], fetch[0]]])
            else:
                subcatrecs.append([name, fetch])
        else:
            cur.execute("select id from valuesproducts where subcategoryviews is not null and productviews is not null "
                        "and subcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, subsubcategoryviews desc, "
                        "productviews desc "
                        "limit 2".format(name))
            fetch = cur.fetchall()
            if len(fetch) == 1:
                subcatrecs.append([name, [fetch[0], fetch[0]]])
            else:
                subcatrecs.append([name, fetch])

for i in range(len(subcatrecs)):
    if subcatrecs[i][1]:
        if subcatrecs[i][0] != 'None':
            for j in range(2):
                cur.execute("UPDATE popular_categorys_per_user SET subcatrecommend = '{}' "
                            "WHERE mostusedsubcat = '{}' "
                            "and catrecommend != '{}' "
                            "and subcatrecommend is null".format(subcatrecs[i][1][j][0], subcatrecs[i][0],
                                                                 subcatrecs[i][1][j][0]))

for i in range(2):
    cur.execute("UPDATE popular_categorys_per_user SET subcatrecommend = '{}' "
                "WHERE subcatrecommend is null and catrecommend != '{}'".format(defaultsubcatrec[i][0],
                                                                                defaultsubcatrec[i][0]))


conn.commit()

print("Calculating subsubcategory recommendations...")

subsubcatrecs = []

for i in range(len(subsubcategorys)):
    if subsubcategorys[i][0]:
        name = subsubcategorys[i][0]
        if "'" in name:
            name = name.split("'")
            name = name[0] + "''" + name[1]
            cur.execute("select id from valuesproducts where subsubcategoryviews is not null "
                        "and productviews is not null "
                        "and subsubcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, subsubcategoryviews desc, "
                        "productviews desc "
                        "limit 2".format(name))
            fetch = cur.fetchall()
            if len(fetch) == 1:
                subsubcatrecs.append([name, [fetch[0], fetch[0], fetch[0]]])
            elif len(fetch) == 2:
                subsubcatrecs.append([name, [fetch[0], fetch[1], fetch[1]]])
            else:
                subsubcatrecs.append([name, fetch])
        else:
            cur.execute("select id from valuesproducts where subsubcategoryviews is not null "
                        "and productviews is not null "
                        "and subsubcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, subsubcategoryviews desc, "
                        "productviews desc "
                        "limit 2".format(name))
            fetch = cur.fetchall()
            if len(fetch) == 1:
                subsubcatrecs.append([name, [fetch[0], fetch[0], fetch[0]]])
            elif len(fetch) == 2:
                subsubcatrecs.append([name, [fetch[0], fetch[1], fetch[1]]])
            else:
                subsubcatrecs.append([name, fetch])

for i in range(len(subsubcatrecs)):
    if subsubcatrecs[i][1]:
        if subsubcatrecs[i][0] != 'None':
            for j in range(3):
                cur.execute("UPDATE popular_categorys_per_user SET subsubcatrecommend = '{}' "
                            "WHERE mostusedsubsubcat = '{}' "
                            "and subcatrecommend != '{}' "
                            "and catrecommend != '{}' "
                            "and subsubcatrecommend is null".format(subsubcatrecs[i][1][j][0], subsubcatrecs[i][0],
                                                                    subsubcatrecs[i][1][j][0],
                                                                    subsubcatrecs[i][1][j][0]))

for i in range(2):
    cur.execute("UPDATE popular_categorys_per_user SET subsubcatrecommend = '{}' "
                "WHERE subsubcatrecommend is null "
                "and catrecommend != '{}' "
                "and subcatrecommend != '{}'".format(defaultsubsubcatrec[i][0], defaultsubsubcatrec[i][0],
                                                     defaultsubsubcatrec[i][0]))

print("Creating table with recommendations per user...")

cur.execute("DROP TABLE IF EXISTS profile_recommendations")

cur.execute("CREATE TABLE profile_recommendations AS (select id, catrecommend, subcatrecommend, subsubcatrecommend "
            "from popular_categorys_per_user)")

print("Recommendations created for user!")

conn.commit()

cur.close()
conn.close()

exec(open('RecommendPerProduct.py').read())
