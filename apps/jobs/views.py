# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import addJob

def index(request):
    context = {
        "addJobs": addJob.objects.all()
	}
    return render(request, 'jobs/index.html', context=context)

def create(request):
    if request.method == 'POST':
        addJob.objects.create(job_title=request.POST['job_title'], job_descp=request.POST['job_descp'])
        return redirect('job:index')

def edit(request, id):
	context = {
		"addJobs": addJob.objects.get(id=int(id))
	}
	return render(request, 'jobs/edit.html', context=context)

def update(request, id):
	errors = addJob.objects.validator(request.POST, "update")
	if len(errors):
		for error in errors.itervalues():
			messages.error(request, error)
		return redirect("/addJob/"+id+"jobs/edit.html")
	else:
		addJob.objects.create(job_title=request.POST['job_title'], job_descp=request.POST['job_descp'])
		return redirect("/addJob/"+id +"jobs/edit.html")

def delete(request,id):
    if addJob.objects.filter(id=id).exists():
        addJob.objects.get(id=id).delete()
    
    return redirect('job:index')
