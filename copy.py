import psycopg2

conn = psycopg2.connect("dbname='prototipo' user='postgres' host='181.143.104.82' password='23826405'")


with conn:

    cur = conn.cursor()
    cur.execute("SELECT * FROM cmg.cmg_usuarios_sstma WHERE cmg.cmg_usuarios_sstma.id_usuario='HMONTOYA'")

    rows = cur.fetchall()

    for row in rows:

        idUser = row[0]
        print(idUseer)
        print(f"{row[0]} {row[1]} {row[2]}")
