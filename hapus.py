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

def Hapus():
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
        jwb = input('apakah anda yakin ingin menghapus data ini? : ')
        if (jwb.upper()=="Y"):
            a = connect()
            sql = "delete FROM customer where idcus = '"+xid+"' "
            a.execute(sql)
            con.commit()
            print('Berhasil Dihapus')
        else :
            print('Data batal dihapus')
    else :
        print('data tidak ditemukan')

Hapus()
