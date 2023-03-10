from django.shortcuts import render

# Create your views here.
def das_HOD(request):
    return render(request,'das_admin.html')

def appr_leav(request):
    return render(request,'approved_leaves.html')

def pend_leav(request):
    return render(request,'pending_leaves.html')

def rej_leav(request):
    return render(request,'pending_leaves.html')