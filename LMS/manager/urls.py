from django.contrib import admin
from django.urls import path
from manager.views import *
from manager import views

urlpatterns = [
    path('manager/',views.dash_man,name="dash_man"),
    path('leaves_mfrm/',leav_mfrm,name="leav_mfrm"),
    path('leaves_mhis/',leav_mhis,name="leav_mhis"),
    path('emp_details/',emp_dts,name="emp_dts"),
    path('emp_leav_details/',emp_leav_dts,name="emp_leav_dts"),
    path('sman_leaves_frm/',sm_leav_frm,name="sm_leav_frm"),
    path('cfrm_emp_leav/<int:empId>',cfrm_emp_leav,name="cfrm_emp_leav"),
    path('man_profile/',views.man_profile,name="man_profile"),
]
