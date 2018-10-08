# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Occupation

def index(request):
    context = {
        "Occupations": Occupation.objects.all()
	}
    return render(request, 'jobs/index.html', context=context)

def create(request):
    if request.method == 'POST':
        Occupation.objects.create(job_title=request.POST['job_title'], job_descp=request.POST['job_descp'])
        return redirect('jobs:index')

def edit(request, id):
	context = {
		"Occupations": Occupation.objects.get(id=int(id))
	}
	return render(request, 'jobs/edit.html', context=context)

def update(request, id):
	print(request.POST["job_descp"])
	errors = Occupation.objects.validator(request.POST)
	if len(errors):
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect(id+"/edit")
	else:
		Occupation.objects.filter(id=int(id)).update(job_title=request.POST['job_title'], job_descp=request.POST['job_descp'])
		return redirect("jobs:show", id=id)

def show(request, id):
	context = {
		"Occupations": Occupation.objects.get(id=int(id))
	}
	return render(request, "jobs/show.html", context)

def delete(request,id):
    if Occupation.objects.filter(id=id).exists():
        Occupation.objects.get(id=id).delete()
    
    return redirect('jobs:index')
