from django.urls import path
from .views import form_view, student_add_api, list_view, student_list_api, student_delete_api, edit_view, \
    student_detail_api,student_api_update

app_name='student'
urlpatterns=[
    path('',form_view,name="form"),
    path('student/add',student_add_api),
    path('student/list',list_view, name="list"),
    path('student/shows',student_list_api),
    path('student/<int:id>/delete',student_delete_api),
    path('student/<int:id>/edit/',edit_view),
    path('student/<int:id>/',student_detail_api),
    path('student/<int:id>/update/',student_api_update)
]