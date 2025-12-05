import mysql.connector as mysql
from datetime import datetime
import info



def save_result():
    db = mysql.connect(host='localhost', user = 'root', password = 'adnansabeer123')
    co = db.cursor()
    co.execute('CREATE DATABASE IF NOT EXISTS VDOC')
    db.commit()
    db.close()

    db = mysql.connect(host='localhost', user = 'root', password = 'adnansabeer123', database = 'VDOC')
    co = db.cursor()
    data = 'CREATE TABLE IF NOT EXISTS RESULT (NAME VARCHAR(200), DOB DATE, SEX VARCHAR(20), BPSYS INT, BPDIA INT, HR INT, O2 DECIMAL(4,1), TEMP DECIMAL(4,2), HT DECIMAL(5,2), WT DECIMAL(5,2), BMI DECIMAL(5,2), BR INT, GLU DECIMAL(6,2), UPH DECIMAL(3,1));'
    co.execute(data)
    db.commit()
    db.close()

def full_checkup_save():
    if info.dob_var:
        dob = datetime.strptime(info.dob_var, "%d-%B-%Y")
        dob_str = dob.strftime("%Y-%m-%d")

    full_name = f"{info.first_name_var} {info.last_name_var}"
    gender = info.gender_var

    db = mysql.connect(host='localhost', user = 'root', password = 'adnansabeer123', database = 'VDOC')
    co = db.cursor()
    data =  """INSERT INTO RESULT VALUES (%s, %s, %s, 118, 76, 72, 97.2, 36.8, 172.25, 68, 23, 16, 92.5, 6.4)"""
    values = (
        full_name,
        dob_str,
        gender
    )
    co.execute(data, values)
    db.commit()
    db.close()