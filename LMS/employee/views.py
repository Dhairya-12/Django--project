from logging import RootLogger
from msilib.schema import Error
from django.shortcuts import render,HttpResponse
import pymysql as mysql
from employee.models import Emp_Leave_app
from manager.models import Man_Leave_app
# Create your views here.
fn=""
ln=""
em=""
mem=""
pwd=0
mob=0
r=""
lty=""
remk=""
depn=""
empc=0
nod=0
std=""
etd=""
stat="Pending"
eid=0


def login(request):
    global em,pwd,r,rol,pas,empc,fn,ema
    if request.method=="POST":
            try:
                con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
                Cursor=con.cursor() 
                d=request.POST
                for key,value in d.items():
                    if key=="email":
                        em=value
                    if key=="password":
                        pwd=value
                    if key=="role":
                        r=value
                q="select password,role,emp_code,first_name from signup_details where email='{}'".format(em)
                Cursor.execute(q)
                result=Cursor.fetchall()[0]
                rol=result[1]
                pas=result[0]
                empc=result[2]
                fn=result[3]
                empc=int(empc)
                print(result)
            except :
                return HttpResponse("err")
            if(r==rol and pwd==pas):
                if(rol=='Employee'):
                    Emp_Leave_applic = Emp_Leave_app.objects.all()
                    return render(request,'das_emp.html', {'Emp_Leave_applic':Emp_Leave_applic,'empc':empc,'fn':fn})
                elif(rol=='Manager'):
                    Emp_Leave_applic = Emp_Leave_app.objects.all()
                    return render(request,'das_manager.html',{'Emp_Leave_applic':Emp_Leave_applic,'empc':empc,'fn':fn})
                elif(rol=='Admin'):
                    Man_Leave_applic = Man_Leave_app.objects.all()
                    return render(request,'das_admin.html',{'Man_Leave_applic':Man_Leave_applic,'empc':empc,'fn':fn})
            else:
                print("error occured")
    return render(request,'login.html')

def signup(request):
    global fn,ln,em,mob,pwd,r,depn,empc
    if request.method=="POST":
            con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
            Cursor=con.cursor() 
            d=request.POST
            for key,value in d.items():
                if key=="first_name":
                    fn=value
                if key=="last_name":
                    ln=value
                if key=="mobile":
                    mob=value
                if key=="emp_code":
                    empc=value
                if key=="dep_name":
                    depn=value
                if key=="role":
                    r=value
                if key=="email":
                    em=value
                if key=="password":
                    pwd=value
            q="insert into signup_details values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,mob,empc,depn,r,em,pwd) 
            Cursor.execute(q)
            con.commit()
             
    return render(request,'signup.html',)


def dash_emp(request):
    Emp_Leave_applic = Emp_Leave_app.objects.all()
    return render(request,'das_emp.html',{'Emp_Leave_applic':Emp_Leave_applic,'empc':empc,'fn':fn})

def leav_frm(request):
    global fn,ln,empc,nod,em,mem,std,etd,lty,remk,stat
    if request.method=="POST":
            con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
            Cursor=con.cursor() 
            d=request.POST
            for key,value in d.items():
                if key=="first_name":
                    fn=value
                if key=="last_name":
                    ln=value
                if key=="emp_code":
                    empc=value
                if key=="no_of_days":
                    nod=value
                if key=="email":
                    em=value
                if key=="m_email":
                    mem=value
                if key=="start_date":
                    std=value
                if key=="end_date":
                    etd=value
                if key=="leave_type":
                    lty=value
                if key=="status":
                    return stat
                if key=="remrk":
                    remk=value
            q="insert into emp_leave_appli values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(eid,fn,ln,empc,nod,em,mem,std,etd,lty,stat,remk) 
            Cursor.execute(q)
            con.commit() 
    return render(request,'leaves_frm.html')

def leav_his(request):
    Emp_Leave_applic = Emp_Leave_app.objects.all()
    return render(request,'leaves_his.html',{'Emp_Leave_applic':Emp_Leave_applic,'empc':empc})

def se_leav_frm(request):
    # con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
    # Cursor=con.cursor() 
    # q="select emp_id from emp_leave_appli"
    # Cursor.execute(q)
    # result=Cursor.fetchall()
    # # print(result)
    Emp_Leave_applic = Emp_Leave_app.objects.all()
    return render(request,'semp_leaves_frm.html',{'Emp_Leave_applic':Emp_Leave_applic})

def emp_profile(request):
    # global fn,ln,r,mob,em,depn,empc,pas
    con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
    Cursor=con.cursor()
    q="select * from signup_details"
    Cursor.execute(q)
    result=Cursor.fetchall()[1]
    fn=result[0]
    ln=result[1]
    mob=result[2]
    empc=result[3]
    depn=result[4]
    r=result[5]
    em=result[6]
    pas=result[7]
    print(result)
    return render(request,'emp_profile.html',{'fn':fn,'ln':ln,'mob':mob,'empc':empc,'r':r,'em':em,'depn':depn,'pas':pas}) 