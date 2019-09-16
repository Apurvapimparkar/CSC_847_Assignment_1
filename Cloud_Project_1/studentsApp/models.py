from django.db import models
from django.urls import reverse

class StudentsInfo(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	student_id = models.CharField(max_length=10, primary_key=True)
	email = models.CharField(max_length=50)
	address = models.TextField()
	gpa = models.CharField(max_length=5)

	def __str__(self):
		return self.student_id 

	def get_absolute_url(self):
		return reverse('student-detail', kwargs={'pk': self.pk})