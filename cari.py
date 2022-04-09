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

def cari():
    global connected
    global con
    global cursor
    xidcus = input('Masukkan id yang dicari : ')
    a = connect()
    sql = "SELECT * FROM customer where idcus = '"+xidcus+"' "
    a.execute(sql)
    if(a!=0):
        
        record = a.fetchall()
        print(record)
        print("search is done.")
    else:
        print('ID yang anda masukkan salah atau tidak terdaftar')
    

cari()