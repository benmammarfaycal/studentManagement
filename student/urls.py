from django.urls import path
from .views import form_view, student_add_api

app_name='student'
urlpatterns=[
    path('',form_view,name="form"),
    path('student/add',student_add_api)
]