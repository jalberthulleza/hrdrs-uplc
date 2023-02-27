from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.models import User, Group
from .models import Employment_Info, Educational_BG, License, Family, Question, Address1, Address2, Address3, Address4, Personal_Info
from .forms import Emp_Info_Form, Educ_BG_Form, License_Form, Family_Form, Question_Form, Address1_Form, Personal_Info_Form

def home_page(request):
	return render(request, 'home.html')

def profile_page(request):
	return render(request, 'employees/employee.html')

def employee_register(request, *args, **kwargs):
	if request.method == 'POST':
		emp_form = Personal_Info_Form(request.POST)
		if emp_form.is_valid():
			emp = emp_form.save(commit=False)
			emp.save()
			return redirect('register')
	else:
		emp_form = Personal_Info_Form()
	return render(request, 'employees/register.html', {'form': emp_form})

def employee_list(request, *arg, **kwargs):
	emp_list = Personal_Info.objects.all()
	return render(request, 'employees/emp_list.html', {'list': emp_list})

def employee_detail(request, pk):
	emp_info = Personal_Info.objects.get(id=pk)
	emp_family = Family.objects.filter(user=emp_info)
	emp_license = License.objects.filter(user=emp_info)

	emp_employment = Employment_Info.objects.get(user=emp_info)
	emp_educ = Educational_BG.objects.get(user=emp_info)
	emp_q = Question.objects.get(user=emp_info)

	if request.method == 'POST':
		# info_form = Personal_Info_Form(request.POST or None, instance=emp_info)
		# emp_form = Emp_Info_Form(request.POST or None, instance=emp_employment)
		# educ_form = Educ_BG_Form(request.POST or None, instance=emp_educ)
		# q_form = Question_Form(request.POST or None, instance=emp_q)
		fam_form = Family_Form(request.POST)
		lic_form = License_Form(request.POST)
		# if info_form.is_valid():
		# 	info_instance = info_form.save(commit=False)
		# 	info_instance.save()
		# 	return redirect('.')
		# elif emp_form.is_valid():
		# 	emp_instance = emp_form.save(commit=False)
		# 	emp_instance.save()
		# 	return redirect('.')
		# elif educ_form.is_valid():
		# 	educ_instance = educ_form.save(commit=False)
		# 	educ_instance.save()
		# 	return redirect('.')
		# elif q_form.is_valid():
		# 	q_instance = q_form.save(commit=False)
		# 	q_instance.save()
		# 	return redirect('.')
		if fam_form.is_valid():
			fam_instance = fam_form.save(commit=False)
			fam_instance.user = emp_info.id
			fam_form.save()
			return redirect('.')
		elif lic_form.is_valid():
			lic_instance = lic_form.save(commit=False)
			lic_instance.user = emp_info.id
			lic_form.save()
	else:
		# info_form = Personal_Info_Form(instance=emp_info)
		# emp_form = Emp_Info_Form(instance=emp_employment)
		# educ_form = Educ_BG_Form(instance=emp_educ)
		# q_form = Question_Form(instance=emp_q)
		fam_form = Family_Form()
		lic_form =License_Form()

	info_form = Personal_Info_Form(request.POST or None, instance=emp_info)
	emp_form = Emp_Info_Form(request.POST or None, instance=emp_employment)
	educ_form = Educ_BG_Form(request.POST or None, instance=emp_educ)
	q_form = Question_Form(request.POST or None, instance=emp_q)
	# fam_form = Family_Form(request.POST)
	# lic_form = License_Form(request.POST)
	if info_form.is_valid():
		info_instance = info_form.save(commit=False)
		info_instance.save()
		return redirect('.')
	elif emp_form.is_valid():
		emp_instance = emp_form.save(commit=False)
		emp_instance.save()
		return redirect('.')
	elif educ_form.is_valid():
		educ_instance = educ_form.save(commit=False)
		educ_instance.save()
		return redirect('.')
	elif q_form.is_valid():
		q_instance = q_form.save(commit=False)
		q_instance.save()
		return redirect('.')
	# elif fam_form.is_valid():
	# 	fam_instance = fam_form.save(commit=False)
	# 	fam_instance.user = emp_info.id
	# 	fam_instance.save()
	# 	return redirect('.')
	# elif lic_form.is_valid():
	# 	lic_instance = lic_form.save(commit=False)
	# 	lic_instance.user = emp_info.id
	# 	lic_instance.save()
	return render(request, 'employees/emp_detail.html', {'info_form': info_form, 'emp_form': emp_form, 'educ_form': educ_form, 'q_form': q_form, 'emp': emp_info, 'emp_family': emp_family, 'emp_license': emp_license, 'fam_form':fam_form, 'lic_form':lic_form})

def employee_fam(request, pk):
	emp_family = Family.objects.get(id=pk)
	fam_form = Family_Form(request.POST or None, instance=emp_family)
	if fam_form.is_valid():
		instance = fam_form.save(commit=False)
		instance.save()
	else:
		fam_form = Family_Form(instance=emp_family)
	return render(request, 'employees/emp_detail_fam.html', {'family': emp_family, 'form':fam_form})

def employee_license(request, pk):
	emp_license = License.objects.get(id=pk)
	form = License_Form(request.POST or None, instance=emp_license)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	else:
		form = License_Form(instance=emp_license)
	return render(request, 'employees/emp_license.html', {'license':emp_license, 'form':form})