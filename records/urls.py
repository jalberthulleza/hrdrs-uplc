from django.contrib.auth import views as av
from django.urls import path
from . import views
from records import views as v

urlpatterns = [
	path('employees/', v.home_page, name='home'),
	path('profile/', v.profile_page, name='profile'),
	path('emp_add/', v.employee_register, name='register'),
	path('emp_list/', v.employee_list, name='list'),
	path('emp_detail/<int:pk>/', v.employee_detail, name='detail'),
	path('emp_detail/family/<int:pk>/', v.employee_fam, name='family'),
	path('emp_detail/license/<int:pk>/', v.employee_license, name='license')
]