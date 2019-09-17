from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import StudentsInfo
from django.contrib import messages
from django.db.models import Q
from django.http import *


def home(request):
	info = {
		'students' : StudentsInfo.objects.all()
	}
	return render(request, 'studentsApp/home.html', info)

class StudentListView(ListView):
	model = StudentsInfo
	template_name = 'studentsApp/home.html'
	context_object_name = 'students'

class StudentSearchListView(ListView):
	model = StudentsInfo
	template_name = 'studentsApp/search.html'
	context_object_name = 'students'
	def get_queryset(self):
		query = self.request.GET.get('q')
		students_search = StudentsInfo.objects.all()
		students_search = StudentsInfo.objects.filter(Q(student_id__icontains=query) | 
								   Q(first_name__icontains=query) |
								   Q(last_name__icontains=query))
		return students_search

class StudentDetailView(DetailView):
	model = StudentsInfo


class StudentCreateView(LoginRequiredMixin, CreateView):
	model = StudentsInfo
	fields = ['first_name', 'last_name', 'student_id', 'email', 'address', 'gpa']


class StudentUpdateView(LoginRequiredMixin, UpdateView):
	model = StudentsInfo
	fields = ['first_name', 'last_name', 'student_id', 'email', 'address', 'gpa']


class StudentDeleteView(LoginRequiredMixin, DeleteView):
	model = StudentsInfo
	success_url = '/'

def about(request):
	return render(request, 'studentsApp/about.html', {'title': 'About'})

