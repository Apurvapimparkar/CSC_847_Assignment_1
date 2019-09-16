import django_filters
from .models import StudentsInfo

class StudentFilter(django_filters.FilterSet):

	class Meta:
        model = StudentsInfo
        fields = ['student_id', 'first_name', 'last_name']