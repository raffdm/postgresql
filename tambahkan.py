import psycopg2 as db
con = None
connected = None
cursor = None
def connect():
    global connected
    global con
    global cursor
    try :
        con = db.connect (host='localhost',database='tokomainan',port =5432,user='postgres',password='raffaeldm201')
        cursor = con.cursor()
        connected = True
    except :
        connected = False
    return cursor

def disconnect():
    global connected
    global con
    global cursor
    if (connected == True):
        cursor.close()
        con.close()
    else :
        con = None
    connected = False

def Tampil(sql):
    a = connect()
    a.execute(sql)
    record = a.fetchall()
    return record

sql = "SELECT * FROM customer"
a = Tampil(sql)
print(a)
disconnect()

def Entry():
    global connected
    global con
    global cursor
    xnama = input('Masukkan Nama Lengkap : ')
    xmainan  = input('Masukkan mainan : ')
    xjml = input('Masukkan banyak mainan : ')
    xhrg = input('Masukkan harga mainan : ')
    a = connect()
    sql = "insert into customer (nama, mainan, jumlah, harga) values ('"+xnama+"','"+xmainan+"','"+xjml+"','"+xhrg+"')"
    a.execute(sql)
    con.commit()
    print('Entry is Done.')

Entry()