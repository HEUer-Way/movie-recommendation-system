import pymysql

def ConnectSql():
    conn = pymysql.connect(host="localhost",port=3306,user='root',password="123456")
    cur = conn.cursor()#生成游标对象
    return conn,cur

def Closesql(conn,cur):
    cur.close()
    conn.close()
    return