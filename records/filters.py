import django_filters
from django.contrib.auth.models import User
from .models import Employment_Info, Educational_BG, License, Family, Question, Address1, Address4, Address3, Address2, Personal_Info
from django.db.models import Q
from django.utils import timezone
import datetime

class DateInput(forms.DateInput):
	input_type = 'date'

class Employment_Info_Filter(django_filters.FilterSet):
	user = django_filters.ModelChoiceFilter(queryset=User.objects.all())
	emp_status = django_filters.CharFilter(lookup_expr='icontains')
	gsis = django_filters.CharFilter(lookup_expr='icontains')
	pagibig = django_filters.CharFilter(lookup_expr='icontains')
	philhealth = django_filters.CharFilter(lookup_expr='icontains')
	sss = django_filters.CharFilter(lookup_expr='icontains')
	tin = django_filters.CharFilter(lookup_expr='icontains')
	agency_emp_no = django_filters.CharFilter(lookup_expr='icontains')
	date_hired = django_filters.DateFilter(lookup_expr='date', widget=DateInput, initial=datetime.date.today)
	date_hired_gt = django_filters.DateFilter(lookup_expr='gte', widget=DateInput)
	date_hired_lt = django_filters.DateFilter(lookup_expr='lte', widget=DateInput)
	present_designation = django_filters.CharFilter(lookup_expr='icontains')
	salary_grade = django_filters.CharFilter(lookup_expr='icontains')
	skills = django_filters.CharFilter(lookup_expr='icontains')
	non_acad_distinction = django_filters.CharFilter(lookup_expr='icontains')
	organization = django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Employment_Info
		fields = {
			user,
			emp_status,
			gsis,
			pagibig,
			philhealth,
			sss,
			tin,
			agency_emp_no,
			date_hired,
			present_designation,
			salary_grade,
			skills,
			non_acad_distinction,
			organization
		}

class Educational_BG_Filter(django_filters.FilterSet):
	c_earned = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Educational_BG
		fields = {
			c_earned
		}

class License_Filter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = License
		fields = {
			name
		}

class Address2_Filter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Address2
		fields = {
			name
		}

class Address3_Filter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Address3
		fields = {
			name
		}

class Address4_Filter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Address4
		fields = {
			name
		}

class Personal_Info_Filter(django_filters.FilterSet):
	s = 'single'
	m = 'married'
	w = 'widowed'
	se = 'separated'
	Civil_Status_Choice = (
			(s, 'Single'),
			(m, 'Married'),
			(w, 'Widowed'),
			(se, 'Separated'),
		)
	a1 = 'A+'
	a2 = 'A-'
	b1 = 'B+'
	b2 = 'B-'
	ab1 = 'AB+'
	ab2 = 'AB-'
	o1 = 'O+'
	o2 = 'O-'
	Blood_Type_Choice = (
			(a1, 'A+'),
			(a2, 'A-'),
			(b1, 'B+'),
			(b2, 'B-'),
			(ab1, 'AB+'),
			(ab2, 'AB-'),
			(o1, 'O+'),
			(o2, 'O-'),
		)
	fil = 'Filipino'
	ali = 'Alien'
	Citizenship_Choice = (
			(fil, 'Filipino'),
			(ali, 'Alien'),
		)
	user = django_filters.ModelChoiceFilter(queryset=User.objects.all())
	employment = django_filters.CharFilter(lookup_expr='icontains')
	middle_name = django_filters.CharFilter(lookup_expr='icontains')
	sex = django_filters.CharFilter(lookup_expr='icontains')
	civil_status = django_filters.ChoiceFilter(choices=Civil_Status_Choice, lookup_expr='iexact')
	blood_type = django_filters.ChoiceFilter(choices=Blood_Type_Choice, lookup_expr='iexact')
	citizenship = django_filters.ChoiceFilter(choices=Citizenship_Choice, lookup_expr='iexact')
	class Meta:
		model = Personal_Info
		fields = {
			user,
			employment,
			middle_name,
			sex,
			civil_status,
			blood_type,
			citizenship
		}