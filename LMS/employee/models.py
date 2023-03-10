from django.db import connections
from django.db import models

# Create your models here.
class Emp_Leave_app(models.Model):
    MY_CHOICE = (
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Pending", "Pending"),
    )
    emp_id = models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=100)
    no_of_days= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    m_email= models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    leave_type=models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=MY_CHOICE, null=True, blank=True, default="Pending")
    remrk=models.CharField(max_length=100,default='Please enter some remark for leave!!')
    class Meta:
        db_table = "Emp_Leave_appli"