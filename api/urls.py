from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="/"),
    path('student-view/<str:pk>/', views.studentView, name="studentview"),
    path('add-student', views.addStudent, name="addstudent"),
    path('update-student/<str:pk>/', views.studentUpdate, name="updatestudent"),
    path('delete-student/<str:pk>/', views.studentDelete, name="deletestudent"),
]