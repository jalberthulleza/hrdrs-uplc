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
	emp_status = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	gsis = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	pagibig = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	philhealth = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	sss = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	tin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	agency_emp_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	date_hired = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	present_designation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	salary_grade = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	skills = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	non_acad_distinction = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	organization = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Employment_Info
		fields = [
			# 'user',
			'emp_status', 'gsis', 'pagibig', 'philhealth', 'sss', 'tin', 'agency_emp_no', 'date_hired', 'present_designation', 'salary_grade', 'skills', 'non_acad_distinction', 'organization']

class Educ_BG_Form(forms.ModelForm):
	e_school_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	e_earned = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	e_graduation_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	e_honors = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	h_school_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	h_earned = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	h_graduation_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	h_honors = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	c_school_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	c_course = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	c_start_year= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	c_end_year= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	c_graduation_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	c_earned = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	c_honors = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	m_school_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	m_course = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	m_start_year= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	m_end_year= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	m_graduation_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	m_earned = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	m_honors = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	d_school_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	d_course = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	d_start_year= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	d_end_year= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	d_graduation_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	d_earned = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	d_honors = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

	
	class Meta:
		model = Educational_BG
		fields = ['e_school_name', 'e_earned', 'e_graduation_date', 'e_honors', 'h_school_name', 'h_earned', 'h_graduation_date', 'h_honors', 'c_school_name', 'c_course', 'c_start_year', 'c_end_year', 'c_graduation_date', 'c_honors', 'm_school_name', 'm_course', 'm_start_year', 'm_end_year', 'm_earned', 'm_graduation_date', 'm_honors', 'd_school_name', 'd_course', 'd_start_year', 'd_end_year', 'd_earned', 'd_graduation_date', 'd_honors']

class License_Form(forms.ModelForm):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	rating = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	exam_place = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	license_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	exam_date = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	validity_date =forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	class Meta:
		model = License
		fields = ['name', 'rating', 'exam_date', 'exam_place', 'license_no', 'validity_date']

class Family_Form(forms.ModelForm):
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	middle_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	relation = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	birthdate = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

	class Meta:
		model = Family
		fields = ['last_name', 'first_name', 'middle_name', 'birthdate','relation']

class Question_Form(forms.ModelForm):
	q1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q4 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q5 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q6 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q7 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q8 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q9 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q10 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q11 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))
	q12 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-check-input', 'type':'checkbox'}))

	class Meta:
		model = Question
		fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12']

class Address1_Form(forms.ModelForm):
	class Meta:
		model = Address1
		fields = ['house', 'street', 'village']

class Personal_Info_Form(forms.ModelForm):
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	middle_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	extension_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	birthdate = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
	birthplace = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	sex = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	civil_status = forms.CharField(max_length=100, widget=forms.DateInput(attrs={'class': 'form-control'}))
	height = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	weight = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	blood_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	citizenship = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	address1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	address2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	address3 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	address4 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	zip_code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	provincial_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	if_province = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	telephone_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	mobile_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_middle_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_extension_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_occupation= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_employer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_business_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_employer = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	s_mobile_no = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	f_first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	f_last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	f_middle_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	f_extension_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	m_last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	m_first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	m_middle_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

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