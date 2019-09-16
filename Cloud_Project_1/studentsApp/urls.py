from django.urls import path
from .views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentSearchListView
from . import views 

urlpatterns = [
    path('', StudentListView.as_view(), name='studentsApp-home'),
    path('student/<pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('new/', StudentCreateView.as_view(), name='student-create'),
    path('student/<pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('search', StudentSearchListView.as_view(),name='search'),
    path('about/', views.about, name='studentsApp-about'),
]