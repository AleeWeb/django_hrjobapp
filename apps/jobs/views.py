# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import addJob

def index(request):
    context = {
		"addJobs": addJob.objects.all()
	}
    return render(request, 'job:index.html')

def create(request):
    if request.method == 'POST':
        addJobs.objects.create(job_title=request.POST['job_title'], job_descp=request.POST['job_descp'])
        return redirect('job:index.html')

def delete(request):
    	return redirect('job:index.html')
