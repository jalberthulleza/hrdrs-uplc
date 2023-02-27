from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from . import Personal_Info

class Address1(models.Model):
	# user = models.ForeignKey(Personal_Info, on_delete=models.DO_NOTHING)
	house = models.CharField(max_length=50)
	street = models.CharField(max_length=100)
	village = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.house} {self.street} {self.village}'

class Address4(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.name}'

class Address3(models.Model):
	name = models.CharField(max_length=100)
	address4 = models.ForeignKey(Address4, on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.name}'

class Address2(models.Model):
	name = models.CharField(max_length=50)
	address3 = models.ForeignKey(Address3, on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.name}'

class Personal_Info(models.Model):
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='account', blank=True, null=True)
	# employment = models.ForeignKey(Employment_Info, on_delete=models.DO_NOTHING, related_name='employment', blank=True, null=True)
	# license = models.ForeignKey(License, on_delete=models.DO_NOTHING, related_name='license', blank=True, null=True)
	# family = models.ForeignKey(Family, on_delete=models.DO_NOTHING, related_name='family', blank=True, null=True)
	# education = models.ForeignKey(Educational_BG, on_delete=models.DO_NOTHING, related_name='education', blank=True, null=True)
	# question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='question', blank=True, null=True)
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	extension_name = models.CharField(max_length=10)
	birthdate = models.DateField()
	birthplace = models.CharField(max_length=50)
	sex = models.CharField(max_length=10)
	civil_status = models.CharField(max_length=50)
	height = models.IntegerField()
	weight = models.IntegerField()
	blood_type = models.CharField(max_length=5)
	citizenship = models.CharField(max_length=50)
	address1 = models.ForeignKey(Address1, on_delete=models.DO_NOTHING, related_name='address1')
	address2 = models.ForeignKey(Address2, on_delete=models.DO_NOTHING, related_name='address2')
	address3 = models.ForeignKey(Address3, on_delete=models.DO_NOTHING, related_name='address3')
	address4 = models.ForeignKey(Address4, on_delete=models.DO_NOTHING, related_name='address4')
	zip_code = models.IntegerField()
	provincial_address = models.CharField(max_length=200)
	if_province = models.BooleanField(default=False)
	telephone_no = models.CharField(max_length=20)
	mobile_no = models.CharField(max_length=20)
	s_last_name = models.CharField(max_length=50)
	s_first_name = models.CharField(max_length=50)
	s_middle_name = models.CharField(max_length=50)
	s_extension_name = models.CharField(max_length=10)
	s_occupation = models.CharField(max_length=50)
	s_employer = models.CharField(max_length=50)
	s_business_address = models.CharField(max_length=100)
	s_mobile_no = models.CharField(max_length=20)
	f_last_name = models.CharField(max_length=50)
	f_first_name = models.CharField(max_length=50)
	f_middle_name = models.CharField(max_length=50)
	f_extension_name = models.CharField(max_length=10)
	m_last_name = models.CharField(max_length=50)
	m_first_name = models.CharField(max_length=50)
	m_middle_name = models.CharField(max_length=50)

	# def __str__(self):
	# 	return f'{self.user.first_name} {self.user.last_name}'

class Employment_Info(models.Model):
	user = models.ForeignKey(Personal_Info, on_delete=models.DO_NOTHING, related_name='e_account')
	emp_status = models.CharField(max_length=50)
	gsis = models.CharField(max_length=50)
	pagibig = models.CharField(max_length=50)
	philhealth = models.CharField(max_length=50)
	sss = models.CharField(max_length=50)
	tin = models.CharField(max_length=50)
	agency_emp_no = models.CharField(max_length=50)
	date_hired = models.DateField()
	present_designation = models.CharField(max_length=50)
	salary_grade = models.IntegerField()
	skills = models.CharField(max_length=200)
	non_acad_distinction = models.CharField(max_length=200)
	organization = models.CharField(max_length=200)

	# def __str__(self):
	# 	return f'{self.user.first_name} {self.user.last_name}'

class Educational_BG(models.Model):
	user = models.ForeignKey(Personal_Info, on_delete=models.DO_NOTHING, related_name='ebg_account')
	e_school_name = models.CharField(max_length=100)
	e_earned = models.CharField(max_length=100)
	e_graduation_date = models.DateField()
	e_honors = models.CharField(max_length=50)
	h_school_name = models.CharField(max_length=100)
	h_earned = models.CharField(max_length=100)
	h_graduation_date = models.DateField()
	h_honors = models.CharField(max_length=50)
	c_school_name = models.CharField(max_length=100)
	c_course = models.CharField(max_length=50)
	c_start_year = models.IntegerField()
	c_end_year = models.IntegerField()
	c_earned = models.CharField(max_length=100)
	c_graduation_date = models.DateField()
	c_honors = models.CharField(max_length=50)
	m_school_name = models.CharField(max_length=100)
	m_course = models.CharField(max_length=50)
	m_start_year = models.IntegerField()
	m_end_year = models.IntegerField()
	m_earned = models.CharField(max_length=100)
	m_graduation_date = models.DateField()
	m_honors = models.CharField(max_length=50)
	d_school_name = models.CharField(max_length=100)
	d_course = models.CharField(max_length=50)
	d_start_year = models.IntegerField()
	d_end_year = models.IntegerField()
	d_earned = models.CharField(max_length=100)
	d_graduation_date = models.DateField()
	d_honors = models.CharField(max_length=50)

	# def __str__(self):
	# 	return f'{self.user.first_name} {self.user.last_name}'

class Question(models.Model):
	user = models.ForeignKey(Personal_Info, on_delete=models.DO_NOTHING, related_name='q_account')
	q1 = models.BooleanField(default=False)
	q1_details = models.CharField(max_length=100, default='W?')
	q2 = models.BooleanField(default=False)
	q2_details = models.CharField(max_length=100, default='W?')
	q3 = models.BooleanField(default=False)
	q3_details = models.CharField(max_length=100, default='W?')
	q4 = models.BooleanField(default=False)
	q4_details = models.CharField(max_length=100, default='W?')
	q5 = models.BooleanField(default=False)
	q5_details = models.CharField(max_length=100, default='W?')
	q6 = models.BooleanField(default=False)
	q6_details = models.CharField(max_length=100, default='W?')
	q7 = models.BooleanField(default=False)
	q7_details = models.CharField(max_length=100, default='W?')
	q8 = models.BooleanField(default=False)
	q8_details = models.CharField(max_length=100, default='W?')
	q9 = models.BooleanField(default=False)
	q9_details = models.CharField(max_length=100, default='W?')
	q10 = models.BooleanField(default=False)
	q10_details = models.CharField(max_length=100, default='Did?')
	q11 = models.BooleanField(default=False)
	q11_details = models.CharField(max_length=100, default='How?')
	q12 = models.BooleanField(default=False)
	q12_details = models.CharField(max_length=100, default='When?')

	# def __str__(self):
	# 	return f'{self.user.first_name} {self.user.last_name}'

class License(models.Model):
	user = models.ForeignKey(Personal_Info, on_delete=models.DO_NOTHING, related_name='l_account')
	name = models.CharField(max_length=50)
	rating = models.IntegerField()
	exam_date = models.DateField()
	exam_place = models.CharField(max_length=100)
	license_no = models.CharField(max_length=50)
	validity_date = models.DateField()

	# def __str__(self):
	# 	return f'{self.user.first_name} {self.user.last_name}'

class Family(models.Model):
	user = models.ForeignKey(Personal_Info, on_delete=models.DO_NOTHING, related_name='f_account')
	# user = models.IntegerField()
	last_name = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	middle_name = models.CharField(max_length=50)
	birthdate = models.DateField()
	relation = models.CharField(max_length=50)

	# def __str__(self):
	# 	return f'{self.first_name}'