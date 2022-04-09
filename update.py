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

def Ubah():
    global connected
    global con
    global cursor
    xid = input('Masukkan ID yang dicari : ')
    a = connect()
    sql = "SELECT * FROM customer where idcus = '"+xid+"' "
    a.execute(sql)
    record = a.fetchall()
    print("Data Saat ini : ")
    print(record)
    row = a.rowcount
    if(row==1):
        print('Silahkan untuk mengubah data..')
        xnama = input('Masukkan Nama Lengkap : ')
        xmainan  = input('Masukkan mainan : ')
        xjml = input('Masukkan banyak mainan : ')
        xhrg = input('Masukkan harga mainan : ')
        a = connect()
        sql = "update customer set nama = '"+xnama+"',mainan = '"+xmainan+"', jumlah = '"+xjml+"', harga = '"+xhrg+"' where idcus = '"+xid+"'" 
        a.execute(sql)
        con.commit()
        print('Update Berhasil')
        sql = "select * from customer where idcus = '"+xid+"'"
        a.execute(sql)
        rec = a.fetchall()
        print ('data setelah diubah')
        print(rec)
Ubah()