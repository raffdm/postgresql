import psycopg2  as db

try:
    con = db.connect(
    host = 'localhost',
    database = 'tokomainan',
    port = 5432,
    user = 'postgres',
    password = 'raffaeldm201')
    cursor = con.cursor()
    print('koneksi berhasil')
except:
    print("koneksi gagal")

