#complete
#student management part 1
import mysql.connector
print("Welcome to Student Management")
print("1.1.New Admission")#WORKING
print("1.2.Update Record") #WORKING
print("1.3.Delete Record")  #WORKING
print("1.4.Display Record") #WORKING
print("1.5.Display Prefectorial Body")#WORKING
c=input("Enter your choice(1.1-1.5): ")
def upr():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    sql = "SELECT * FROM class12"
    mc.execute(sql)
    k=int(input("Enter Admission Number to be Updated"))
    s=mc.fetchall()
    for i in s:
        i=list(i)
        if i[0]==k:
            print(i)
            L=input("Do you want to update Admission no? [y/n]")
            if L=='y' or L=='Y':
                i[0]=input("Enter admission number")
            M=input("Do you want to update First Name ? [y/n]")
            if M=='y' or M=='Y':
                i[1]=input("Enter First Name ")
            O=input("Do you want to update Last Name  [y/n]")
            if O=='y' or O=='Y':
                i[2]=input("Enter Last Name")
            P=input("Do you want to update class? [y/n]")
            if P=='y' or P=='Y':
                i[3]=int(input("Enter class:"))
            Q=input("Do you want to update date of birth?")
            if Q=='y' or Q=='Y':
                i[4]=input("Enter date of birth:")
            R=input("Do you want to update date of admission?")
            if R=='y' or R=='Y':
                i[5]=input("Enter date of admission:")
            S=input("Do you want to update sibling?")
            if S=='y' or S=='Y':
                i[6]=input("Enter status of sibling:")
            T=input("Do you want to update sibling name?")
            if T=='y' or T=='Y':
                i[7]=input("Enter sibling name:")
            U=input("Do you want to change mother name?")
            if U=='y' or U=='Y':
                i[8]=input("Enter mother name:")
            V=input("Do you want to update father name?")
            if V=='y' or V=='Y':
                i[9]=input("Enter father name:")
            W=input("Do you want to update phone number?")
            if W=='y' or W=='Y':
                i[10]=input("Enter phone number:")
            X=input("Do you want to update transport?")
            if X=='y' or X=='Y':
                i[11]=input("Enter transport:")
            Y=input("Do you want to update date of birth?")
            if Y=='y' or Y=='Y':
                i[12]=input("Enter stream:")
            cmd="update class12 set ADMISSION_NO=%s,NAME=%s,  L_NAME=%s, CLASS=%s, DOB=%s,  DOJ=%s, SIBLING=%s,SIBLING_NAME=%s, MOTHER_NAME=%s,  FATHER_NAME=%s,  PHONE_NO=%s, TRANSPORT=%s, STREAM=%s "
            rec=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12])
            mc.execute(cmd,rec)
            db.commit()
            print("Record Data Updated")
            print(i)
            break

def disr():
    try:
        db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
        cursor = db.cursor()
        sql = "SELECT * FROM class12"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
           admno=c[0]
           n=c[1]
           ln=c[2]
           cls=c[3]
           dob=c[4]
           doj=c[5]
           sb=c[6]
           sbn=c[7]
           mn=c[8]
           fn=c[9]
           ph=c[10]
           tr=c[11]
           st=c[12]
           print ("(admission_no=%s,name=%s,last_name=%s,claas=%s,dob=%s,doj=%s,sb=%s,sbname=%s,mothern=%s,fathern=%s,phone=%s,transport=%s,stream=%s)" % (admno,n,ln,cls,dob,doj,sb,sbn,mn,fn,ph,tr,st))
    except:
        print ("Error: unable to fetch data")
        db.close()
def newad():
    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    admno=input("Enter admission number:")
    n=input("Enter first name:")
    ln=input("Enter last name:")
    cls=input("Enter class:")
    dob=input("Enter date of birth:")
    doj=input("Enter date of admission:")
    sb=input("Enter status of sibling[Y/N]:")
    sbn=input("Enter sibling name:")
    mn=input("Enter mother name:")
    fn=input("Enter fathers name:")
    ph=input("Enter phone number:")
    tr=input("Enter mode of transport:")
    st=input("Enter stream:")
    val=(admno,n,ln,cls,dob,doj,sb,sbn,mn,fn,ph,tr,st)
    sql="insert into CLASS12 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mc.execute(sql,val)
    db.commit()
    print("record added successfully!")
def delr():
    temp=int(input("Enter admission number to be deleted : "))

    db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
    mc= db.cursor()
    try:
        sql = "delete from class12 where admission_no='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            mc.execute(sql)
            db.commit()
            print("successfully deleted")
    except Exception as e:
        print (e)
        db.close()
def disp():
    try:
        db = mysql.connector.connect(user='root', password='nandanasql', host='localhost',database='project')
        cursor = db.cursor()
        sql = "SELECT * FROM prefectorial_body"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
           n=c[0]
           cls=c[1]
           desig=c[2]
           print ("(name=%s,class=%s,desig=%s)" % (n,cls,desig))
    except:
        print ("Error: unable to fetch data")
        db.close()

if c=="1.1":
    newad()
elif c=="1.2":
    upr()
elif c=="1.3":
    delr()
elif c=="1.4":
    disr()
elif c=="1.5":
    disp()
else:
    print("Invalid choice")


