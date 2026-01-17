from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import student
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def form_view(request):
    return render(request,'student/index.html')

@csrf_exempt
def student_add_api(request):
    if request.method=='POST':
        data=json.loads(request.body)
        prenom=data.get('prenom')
        note=data.get('note')
        etudiant=student(
            prenom=prenom,
            note=note
        )
        etudiant.save()

    return JsonResponse({"status":"ok"})

def list_view(request):
    return render(request,'student/student_list.html')

def student_list_api(request):
    students=list(student.objects.values('id','prenom','note'))
    return JsonResponse(students,safe=False)

@csrf_exempt
def student_delete_api(request,id):
    students=student.objects.get(id=id)
    students.delete()
    return JsonResponse({"status":"ok"})

def edit_view(request,id):
    return render(request,'student/edit.html',{"id":id})

