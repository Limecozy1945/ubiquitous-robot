#COMPLETE
#teacher management cs project
import mysql.connector
print("Welcome to Teacher Management")
print("1.1.New Employee")#WORKING
print("1.2.Update Record") #WORKING
print("1.3.Delete Record") #WORKING
print("1.4.Display Records")#WORKING
print("1.5.Display HODS") #WORKING
print("1.6.Display Emails") #WORKING
print("1.7.Search Record") #WORKING

c=input("Enter your choice(1.1-1.7): ")
def newe():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    n=input("Enter first name:")
    doj=input("Enter date of join:")
    s=input("enter salary")
    d=input("Enter description:")
    dob=input("Enter date of birth:")
    g=input("Enter gender:")
    val=(n,doj,s,d,dob,g)
    sql="insert into teachers values(%s,%s,%s,%s,%s,%s)"
    mc.execute(sql,val)
    db.commit()
    print("record added successfully!")

def disem():
    db=mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc=db.cursor()
    mc.execute("SELECT * from teachers")
    S=mc.fetchall()
    for i in S:
        i=list(i)
        print(i[0],i[1],i[2],i[3],i[4],i[5])
def upe():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    sql = "SELECT * FROM TEACHERS"
    mc.execute(sql)
    k=input("Enter NAME to be Updated: ")
    s=mc.fetchall()
    for i in s:
        i=list(i)
        if i[0]==k:
            print(i)
            L=input("Do you want to update NAME? [y/n]")
            if L=='y' or L=='Y':
                i[0]=input("Enter NAME:")
            M=input("Do you want to update DOJ ? [y/n]")
            if M=='y' or M=='Y':
                i[1]=input("Enter DOJ ")
            O=input("Do you want to update SALARY[y/n]")
            if O=='y' or O=='Y':
                i[2]=input("Enter SALARY:")
            P=input("Do you want to update DESIGNATION? [y/n]")
            if P=='y' or P=='Y':
                i[3]=input("Enter DESIGNATION:")
            Q=input("Do you want to update DOB?")
            if Q=='y' or Q=='Y':
                i[4]=input("Enter DOB:")
            R=input("Do you want to update GENDER?")
            if R=='y' or R=='Y':
                i[5]=input("Enter GENDER:")
            
            cmd="update teachers set NAME=%s,DOJ=%s,SALARY=%s,DESCRIPTION=%s, DOB=%s,GENDER=%s where NAME=%s"
            rec=(i[0],i[1],i[2],i[3],i[4],i[5],k)
            mc.execute(cmd,rec)
            db.commit()
            print("Record Data Updated")
            print(i)
            break
def dele():
    temp=input("Enter EMP_NO to be deleted : ")

    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    try:
        sql = "delete from teachers where EMP_NO='%s'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            mc.execute(sql)
            db.commit()
            print("successfully deleted")
    except Exception as e:
        print (e)
        db.close()
def secr():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    mc.execute('select* from TEACHERS')
    s=mc.fetchall()
    j=int(input("Enter Employee Number to be Searched:"))
    for i in s:
        i=list(i)
        if i[0]==j:
            c='select * from TEACHERS where EMP_NO=%s'
            v=(i[0],)
            mc.execute(c,v)
            for i in mc:
                print(i)
            break
    else:
        print("Invalid record")
def dishod():
    db=mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc=db.cursor()
    mc.execute("SELECT * from HOD")
    S=mc.fetchall()
    for i in S:
        i=list(i)
        print(i[0],i[1])
def disem():
    db=mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc=db.cursor()
    mc.execute("SELECT * from emails")
    S=mc.fetchall()
    for i in S:
        i=list(i)
        print(i[0],i[1])
if c=="1.1":
    newe()
elif c=="1.2":
    upe()
elif c=="1.3":
    dele()
elif c=="1.4":
    disem()
elif c=="1.5":
    dishod()
elif c=="1.6":
    disem()
elif c=='1.7':
    secr()
else:
    print("Invalid choice")
