from django.contrib import admin
from django.urls import path
from employee.views import *
from employee import views

urlpatterns = [
    path('',login,name="login"),
    path('signup/',signup,name="signup"),
    path('emp/',views.dash_emp,name="dash_emp"),
    path('leaves_frm/',views.leav_frm,name="leav_frm"),
    path('Leaveshis/',views.leav_his,name="leav_his"),
    path('semp_leaves_frm/',views.se_leav_frm,name="se_leav_frm"),
    path('emp_profile/',views.emp_profile,name="emp_profile"),
]
