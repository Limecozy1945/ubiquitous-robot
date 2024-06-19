#fee management cs project

def upre():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    sql = "SELECT * FROM fees"
    mc.execute(sql)
    k=input("Enter Class to be Updated")
    s=mc.fetchall()
    for i in s:
        i=list(i)
        if i[0]==k:
            print(i)
            M=input("Do you want to update TUTION_FEES? [y/n]")
            if M=='y' or M=='Y':
                i[1]=int(input("Enter TUTION FEES:"))
            O=input("Do you want to update ADMISSION FEES [y/n]")
            if O=='y' or O=='Y':
                i[2]=int(input("Enter ADMISSION FEES:"))
            P=input("Do you want to update TERM FEES? [y/n]")
            if P=='y' or P=='Y':
                i[3]=int(input("Enter TERM FEES:"))
            Q=input("Do you want to update STATIONARY_FEES?")
            if Q=='y' or Q=='Y':
                i[4]=int(input("Enter STATIONARY FEES:"))
            R=input("Do you want to update EXAM FEES?")
            if R=='y' or R=='Y':
                i[5]=int(input("Enter EXAM FEES:"))
            S=input("Do you want to update INSURANCE FEES?")
            if S=='y' or S=='Y':
                i[6]=int(input("Enter INSURANCE FEES:"))
            T=input("Do you want to update COMPUTER LAB FEES?")
            if T=='y' or T=='Y':
                i[7]=int(input("Enter COMPUTER LAB FEES:"))
            U=input("Do you want to change LABATORY FEES?")
            if U=='y' or U=='Y':
                i[8]=int(input("Enter LABATORY FEES:"))
            V=input("Do you want to update COMPULSORY DEPOSIT?")
            if V=='y' or V=='Y':
                i[9]=int(input("Enter COMPULOSORY DEPOSIT:"))
            W=input("Do you want to update REFUNDABLE DEPOSIT?")
            if W=='y' or W=='Y':
                i[10]=int(input("Enter REFUNDABLE DEPOSIT:"))
            X=input("Do you want to update TOTAL?")
            if X=='y' or X=='Y':
                i[11]=int(input("Enter TOTAL:"))
            Y=input("Do you want to update ?")
            
            cmd="update fees set TUTION_FEES=%d, ADMISSION_FEES=%d,TERM_FEES=%d,STATIONARY_FEES=%d,EXAMINATION_FEES=%d,INSURANCE_FEES=%d,COMPUTER_LAB_FEES=%d, LABATORY_FEES=%d,COMPULOSORY_DEPOSIT=%d,REFUNDABLE_DEPOSIT=%d,TOTAL=%d"
            rec=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11])
            mc.execute(cmd,rec)
            db.commit()
            print("Record Data Updated")
            print(i)
            break
def delre():
    temp=input("Enter CLASS to be deleted : ")

    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    try:
        sql = "delete from FEES where CLASS='%s'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            mc.execute(sql)
            db.commit()
            print("successfully deleted")
    except Exception as e:
        print (e)
        db.close()
def dispre():
    db=mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc=db.cursor()
    mc.execute("SELECT * from fees")
    S=mc.fetchall()
    for i in S:
        i=list(i)
        print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],)
def seare():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    sql = "SELECT * FROM fees"
    mc.execute(sql)
    j=input("Enter Class to be Searched:")
    s=mc.fetchall()
    for i in s:
        i=list(i)
        if i[0]==j:
            print(i)


import mysql.connector
print("Welcome to Fee Management")
print("1.1.Update Record") 
print("1.2.Delete Record")  #WORKING
print("1.3.Display Full Record") #WORKING
print("1.4.Search Record") #WORKING
for x in range(4):
    c=input("Enter your choice(1.1-1.4): ")
    if c=="1.1":
       upre()
    elif c=="1.2":
        delre()
    elif c=="1.3":
        dispre()
    elif c=="1.4":
        seare()
    else:
        print("Invalid choice")
