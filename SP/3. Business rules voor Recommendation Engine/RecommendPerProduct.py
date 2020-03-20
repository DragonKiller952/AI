import psycopg2

print("\n### RecommendPerProduct.py ###\n")

conn = psycopg2.connect("dbname=Onlinestore user=postgres password=0Ksndjskxw")
cur = conn.cursor()

print("Setting up tables...")

cur.execute("DROP TABLE IF EXISTS valuesproducts")

cur.execute("CREATE TABLE valuesproducts AS (select id, name, targetaudience, brand, category, subcategory, "
            "subsubcategory, categoryviews, subcategoryviews, subsubcategoryviews, productviews from products)")

cur.execute("ALTER TABLE products DROP COLUMN IF EXISTS catrecommend")
cur.execute("ALTER TABLE products DROP COLUMN IF EXISTS subcatrecommend")
cur.execute("ALTER TABLE products DROP COLUMN IF EXISTS subsubcatrecommend")

cur.execute("ALTER TABLE products ADD catrecommend varchar")
cur.execute("ALTER TABLE products ADD subcatrecommend varchar")
cur.execute("ALTER TABLE products ADD subsubcatrecommend varchar")

conn.commit()

print("Getting data...")

cur.execute("select category from products")

categorys = list(set(cur.fetchall()))

cur.execute("select id from valuesproducts where categoryviews is not null and subcategoryviews is not null and"
            " subsubcategoryviews is not null and productviews is not null "
            "order by categoryviews desc,  subcategoryviews desc, subsubcategoryviews desc, productviews desc "
            "limit 1")

defaultcatrec = cur.fetchall()

cur.execute("select subcategory from products")

subcategorys = list(set(cur.fetchall()))

cur.execute("select id from valuesproducts where subcategoryviews is not null and"
            " subsubcategoryviews is not null and productviews is not null "
            "order by subcategoryviews desc, subsubcategoryviews desc, productviews desc "
            "limit 2")

defaultsubcatrec = cur.fetchall()

cur.execute("select subsubcategory from products")

subsubcategorys = list(set(cur.fetchall()))

cur.execute("select id from valuesproducts where subsubcategoryviews is not null and productviews is not null "
            "order by subsubcategoryviews desc, productviews desc "
            "limit 3")

defaultsubsubcatrec = cur.fetchall()

print("Calculating category recommendations...")

catrecs = []

for i in range(len(categorys)):
    if categorys[i][0]:
        if '[' not in categorys[i][0]:
            cur.execute("select id from valuesproducts where categoryviews is not null and "
                        "productviews is not null and category = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, "
                        "subsubcategoryviews desc, productviews desc "
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
                cur.execute("UPDATE products SET catrecommend = '{}' "
                            "WHERE category = '{}'".format(catrecs[i][1][0][0], name))
            else:
                cur.execute("UPDATE products SET catrecommend = '{}' "
                            "WHERE category = '{}'".format(catrecs[i][1][0][0], name))


cur.execute("UPDATE products SET catrecommend = '{}' "
            "WHERE catrecommend is null".format(defaultcatrec[0][0]))

conn.commit()

print("Calculating subcategory recommendations...")

subcatrecs = []

for i in range(len(subcategorys)):
    name = subcategorys[i][0]
    if subcategorys[i][0]:
        if "'" in name:
            name = name.split("'")
            name = name[0] + "''" + name[1]
            cur.execute("select id from valuesproducts where subcategoryviews is not null and productviews is not null "
                        "and subcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, "
                        "subsubcategoryviews desc, productviews desc "
                        "limit 2".format(name))
            fetch = cur.fetchall()
            if len(fetch) == 1:
                subcatrecs.append([name, [fetch[0], fetch[0]]])
            else:
                subcatrecs.append([name, fetch])
        else:
            cur.execute("select id from valuesproducts where subcategoryviews is not null and productviews is not null "
                        "and subcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, "
                        "subsubcategoryviews desc, productviews desc "
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
                cur.execute("UPDATE products SET subcatrecommend = '{}' "
                            "WHERE subcategory = '{}' "
                            "and catrecommend != '{}' "
                            "and subcatrecommend is null".format(subcatrecs[i][1][j][0], subcatrecs[i][0],
                                                                 subcatrecs[i][1][j][0]))

for i in range(2):
    cur.execute("UPDATE products SET subcatrecommend = '{}' "
                "WHERE subcatrecommend is null and catrecommend != '{}'".format(defaultsubcatrec[i][0], defaultsubcatrec[i][0]))


conn.commit()

print("Calculating subsubcategory recommendations...")

subsubcatrecs = []

for i in range(len(subsubcategorys)):
    if subsubcategorys[i][0]:
        name = subsubcategorys[i][0]
        if "'" in name:
            name = name.split("'")
            name = name[0] + "''" + name[1]
            cur.execute("select id from valuesproducts where subsubcategoryviews is not null and "
                        "productviews is not null and subsubcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, "
                        "subsubcategoryviews desc, productviews desc "
                        "limit 2".format(name))
            fetch = cur.fetchall()
            if len(fetch) == 1:
                subsubcatrecs.append([name, [fetch[0], fetch[0], fetch[0]]])
            elif len(fetch) == 2:
                subsubcatrecs.append([name, [fetch[0], fetch[1], fetch[1]]])
            else:
                subsubcatrecs.append([name, fetch])
        else:
            cur.execute("select id from valuesproducts where subsubcategoryviews is not null and "
                        "productviews is not null and subsubcategory = '{}'"
                        "order by categoryviews desc, subcategoryviews desc, "
                        "subsubcategoryviews desc, productviews desc "
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
                cur.execute("UPDATE products SET subsubcatrecommend = '{}' "
                            "WHERE subsubcategory = '{}' "
                            "and subcatrecommend != '{}' "
                            "and catrecommend != '{}' "
                            "and subsubcatrecommend is null".format(subsubcatrecs[i][1][j][0], subsubcatrecs[i][0],
                                                                 subsubcatrecs[i][1][j][0], subsubcatrecs[i][1][j][0]))

for i in range(2):
    cur.execute("UPDATE products SET subsubcatrecommend = '{}' "
                "WHERE subsubcatrecommend is null "
                "and catrecommend != '{}' "
                "and subcatrecommend != '{}'".format(defaultsubsubcatrec[i][0], defaultsubsubcatrec[i][0],
                                                     defaultsubsubcatrec[i][0]))

print("Creating table with recommendations per product...")

cur.execute("DROP TABLE IF EXISTS product_recommendations")

cur.execute("CREATE TABLE product_recommendations AS (select id, catrecommend, subcatrecommend, subsubcatrecommend "
            "from products)")

print("Recommendations created for products!")

conn.commit()

cur.close()
conn.close()
