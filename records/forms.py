from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from .models import Employment_Info, Educational_BG, License, Family, Question, Address1, Address4, Address3, Address2, Personal_Info
import datetime

class DateInput(forms.DateInput):
	input_type = 'date'
class TimeInput(forms.TimeInput):
	input_type = 'time'

class Emp_Info_Form(forms.ModelForm):
	date_hired = forms.DateField(widget=DateInput)
	class Meta:
		model = Employment_Info
		fields = [
			# 'user',
			'emp_status', 'gsis', 'pagibig', 'philhealth', 'sss', 'tin', 'agency_emp_no', 'date_hired', 'present_designation', 'salary_grade', 'skills', 'non_acad_distinction', 'organization']

class Educ_BG_Form(forms.ModelForm):
	e_graduation_date = forms.DateField(widget=DateInput)
	h_graduation_date = forms.DateField(widget=DateInput)
	c_start_year = forms.DateField(widget=DateInput)
	c_end_year = forms.DateField(widget=DateInput)
	c_graduation_date = forms.DateField(widget=DateInput)
	m_start_year = forms.DateField(widget=DateInput)
	m_end_year = forms.DateField(widget=DateInput)
	m_graduation_date = forms.DateField(widget=DateInput)
	d_start_year = forms.DateField(widget=DateInput)
	d_end_year = forms.DateField(widget=DateInput)
	d_graduation_date = forms.DateField(widget=DateInput)
	class Meta:
		model = Educational_BG
		fields = ['e_school_name', 'e_earned', 'e_graduation_date', 'e_honors', 'h_school_name', 'h_earned', 'h_graduation_date', 'h_honors', 'c_school_name', 'c_course', 'c_start_year', 'c_end_year', 'c_graduation_date', 'c_honors', 'm_school_name', 'm_course', 'm_start_year', 'm_end_year', 'm_earned', 'm_graduation_date', 'm_honors', 'd_school_name', 'd_course', 'd_start_year', 'd_end_year', 'd_earned', 'd_graduation_date', 'd_honors']

class License_Form(forms.ModelForm):
	exam_date = forms.DateField(widget=DateInput)
	validity_date = forms.DateField(widget=DateInput)
	class Meta:
		model = License
		fields = ['name', 'rating', 'exam_date', 'exam_place', 'license_no', 'validity_date']

class Family_Form(forms.ModelForm):
	birthdate = forms.DateField(widget=DateInput)
	class Meta:
		model = Family
		fields = ['last_name', 'first_name', 'middle_name', 'birthdate','relation']

class Question_Form(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']

class Address1_Form(forms.ModelForm):
	class Meta:
		model = Address1
		fields = ['house', 'street', 'village']

class Personal_Info_Form(forms.ModelForm):
	birthdate = forms.DateField(widget=DateInput)
	class Meta:
		model = Personal_Info
		fields = [
			# 'employment',
			# 'license',
			# 'family',
			# 'education',
			# 'question',
			'first_name',
			'middle_name',
			'last_name',
			'email',
			'extension_name',
			'birthdate',
			'birthplace',
			'sex',
			'civil_status',
			'height',
			'weight',
			'blood_type',
			'citizenship',
			'address1',
			'address2',
			'address3',
			'address4',
			'zip_code',
			'provincial_address',
			'if_province',
			'telephone_no',
			'mobile_no',
			's_last_name',
			's_first_name',
			's_middle_name',
			's_extension_name',
			's_occupation',
			's_employer',
			's_business_address',
			's_mobile_no',
			'f_last_name',
			'f_first_name',
			'f_middle_name',
			'f_extension_name',
			'm_last_name',
			'm_first_name',
			'm_middle_name'
		]