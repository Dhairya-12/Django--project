from django.shortcuts import render,redirect
from employee.models import Emp_Leave_app
import pymysql as mysql

# Create your views here.
fn=""
ln=""
empc=""
mob=""
dep=""
r=""
em=""
stat=""
eid=0
std=""
demo=""
def dash_man(request):
    Emp_Leave_applic = Emp_Leave_app.objects.all()
    return render(request,"das_manager.html",{'Emp_Leave_applic':Emp_Leave_applic})


def leav_mfrm(request):
    return render(request,'leaves_mfrm.html')

def leav_mhis(request):
    return render(request,'leaves_mhis.html')

def emp_dts(request):
    global fn,ln,r,mob,em,dep,empc
    con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
    Cursor=con.cursor() 
    q="select * from signup_details"
    Cursor.execute(q)
    result=Cursor.fetchall()[0]
    fn=result[0]
    ln=result[1]
    mob=result[2]
    empc=result[3]
    dep=result[4]
    r=result[5]
    em=result[6]

    return render(request,'emp_details.html',{'fn':fn,'ln':ln,'mob':mob,'empc':empc,'r':r,'em':em,'dep':dep})

def emp_leav_dts(request):
    Emp_Leave_applic = Emp_Leave_app.objects.all()
    return render(request,'emp_leav_details.html',{'Emp_Leave_applic':Emp_Leave_applic})


def cfrm_emp_leav(request,empId):
    global std,etd,stat,demo
    if request.method=="POST":
            con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
            Cursor=con.cursor() 
            d=request.POST
            for key,value in d.items():
                if key=="start_date":
                    std=value
                if key=="end_date":
                    etd=value
                if key=="status":
                    stat=value
            q="update emp_leave_appli set status='{}' where start_date='{}' and end_date='{}' and emp_id={}".format(stat,std,etd,empId) 
            Cursor.execute(q)
            con.commit()
    Emp_Leave_applic = Emp_Leave_app.objects.all()
    # employee = Emp_Leave_app.objects.filter(emp_id=empId)
    # print(employee)
    return render(request,'cfrm_emp_leav.html',{'Emp_Leave_applic':Emp_Leave_applic,'std':std,'empId':empId})

