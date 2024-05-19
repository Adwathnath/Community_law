import pymysql

def selectone(qry,value):
    con = pymysql.connect(host="localhost", user="root", password="1234", port=3306, database="community_law_db")
    cmd = con.cursor()
    cmd.execute(qry,value)
    res=cmd.fetchone()
    return res

def iud(qry,value):
    con=pymysql.connect(host="localhost",user="root",password="1234",port=3306,database="community_law_db")
    cmd=con.cursor()
    cmd.execute(qry,value)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id