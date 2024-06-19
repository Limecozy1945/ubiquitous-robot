#exam management cs project
import mysql.connector
print("Welcome to Exam Management")
print("4.0.Add Record")#WORKING
print("4.1.Update Record") #WORKING
print("4.2.Delete Record")  #WORKING
print("4.3.Display Full Record") #WORKING
print("4.4.Search Record")#WORKING

def addrec():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    n=input("Enter name of exam:")
    doj=input("Enter day:")
    s=input("enter month")
    d=input("Enter year:")
    dob=input("Enter class:")
    g=input("Enter subject:")
    val=(n,doj,s,d,dob,g)
    sql="insert into exam values(%s,%s,%s,%s,%s,%s)"
    mc.execute(sql,val)
    db.commit()
    print("record added successfully!")
def displayrec():
    db=mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc=db.cursor()
    mc.execute("SELECT * from EXAM")
    S=mc.fetchall()
    for i in S:
        i=list(i)
        print(i[0],i[1],i[2],i[3],i[4],i[5])
def updaterec():
     db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
     mc= db.cursor()
     sql = "SELECT * FROM EXAM"
     mc.execute(sql)
     k=input("Enter NAME_OF_EXAM to be Updated: ")
     s=mc.fetchall()
     for i in s:
         i=list(i)
         if i[0]==k:
             print(i)
             L=input("Do you want to update Name of Exam? [y/n]")
             if L=='y' or L=='Y':
                 i[0]=input("Enter Name of Exam:")
             M=input("Do you want to update Day? [y/n]")
             if M=='y' or M=='Y':
                 i[1]=input("Enter Day ")
             O=input("Do you want to update Month[y/n]")
             if O=='y' or O=='Y':
                 i[2]=input("Enter Month:")
             P=input("Do you want to update Year? [y/n]")
             if P=='y' or P=='Y':
                 i[3]=input("Enter Year:")
             Q=input("Do you want to update Class?")
             if Q=='y' or Q=='Y':
                 i[4]=input("Enter Class:")
             R=input("Do you want to update Subject?")
             if R=='y' or R=='Y':
                 i[5]=input("Enter Subject:")
            
             cmd="update exam set NAME_OF_EXAM=%s,DAY=%s,MONTH=%s,YEAR=%s,CLASS=%s,SUBJECT=%s"
             rec=(i[0],i[1],i[2],i[3],i[4],i[5])
             mc.execute(cmd,rec)
             db.commit()
             print("Record Data Updated")
             print(i)
             break
def deleterec():
    temp=input("Enter NAME_OF_EXAM to be deleted : ")
    #cls=int(input("Enter  CLASS : "))
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    try:
        sql = "delete from EXAM where NAME_OF_EXAM='%s'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            mc.execute(sql)
            db.commit()
            print("successfully deleted")
    except Exception as e:
        print (e)
        db.close()
def searchrec():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    mc.execute('select* from EXAM')
    s=mc.fetchall()
    j=input("Enter EXAM NAME to be Searched:")
    for i in s:
        i=list(i)
        if i[0]==j:
            c='select * from  EXAM where NAME_OF_EXAM=%s'
            v=(i[0],)
            mc.execute(c,v)
            for i in mc:
                print(i)
            break
    else:
        print("Invalid record")
    
#for x in range(4):
c=input("Enter your choice(4.1-4.4): ")
if c=="4.0":
    addrec()
elif c=="4.1":
    updaterec()
elif c=="4.2":
    deleterec()
elif c=="4.3":
    displayrec()
elif c=="4.4":
    searchrec()
else:
    print("Invalid choice")
