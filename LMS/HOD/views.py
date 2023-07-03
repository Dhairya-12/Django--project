from django.shortcuts import render,redirect
from manager.models import Man_Leave_app
import pymysql as mysql

# Create your views here.
fn=""
ln=""
empc=0
mob=""
dep=""
r=""
em=""
aem=""
stat="Pending"
eid=0
std=""
etd=""
lty=""
demo=""
remk=""



def das_HOD(request):
    Man_Leave_applic = Man_Leave_app.objects.all()
    return render(request,"das_admin.html",{'Man_Leave_applic':Man_Leave_applic})

def appr_leav(request):
    Man_Leave_applic = Man_Leave_app.objects.all()
    return render(request,'approved_leaves.html',{'Man_Leave_applic':Man_Leave_applic})

def pend_leav(request):
    Man_Leave_applic = Man_Leave_app.objects.all()
    return render(request,'pending_leaves.html',{'Man_Leave_applic':Man_Leave_applic})

def rej_leav(request):
    Man_Leave_applic = Man_Leave_app.objects.all()
    return render(request,'rejected_leaves.html',{'Man_Leave_applic':Man_Leave_applic})

def cfrm_man_leav(request,empId):
    global std,etd,stat
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
            q="update man_leave_appli set status='{}' where start_date='{}' and end_date='{}' and emp_id={}".format(stat,std,etd,empId) 
            Cursor.execute(q)
            con.commit()
    Man_Leave_applic = Man_Leave_app.objects.all()
    return render(request,'cfrm_man_leav.html',{'Man_Leave_applic':Man_Leave_applic,'std':std,'empId':empId})

def hr_profile(request):
    # global fn,ln,r,mob,em,depn,empc,pas
    con=mysql.connect(host="localhost",user="root",passwd="",database="lms") 
    Cursor=con.cursor()
    q="select * from signup_details"
    Cursor.execute(q)
    result=Cursor.fetchall()[0]
    fn=result[0]
    ln=result[1]
    mob=result[2]
    empc=result[3]
    depn=result[4]
    r=result[5]
    em=result[6]
    pas=result[7]
    print(result)
    return render(request,'hr_profile.html',{'fn':fn,'ln':ln,'mob':mob,'empc':empc,'r':r,'em':em,'depn':depn,'pas':pas})