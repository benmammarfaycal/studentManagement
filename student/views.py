from django.http import JsonResponse
from django.shortcuts import render
import json
from .models import Student
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
        etudiant=Student(
            prenom=prenom,
            note=note
        )
        etudiant.save()

    return JsonResponse({"status":"ok"})