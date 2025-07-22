from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

def index(request):
    all_person = Person.objects.all()
    return render(request,"index.html",{"all_person":all_person})

def about(request):
    return render(request,"about.html")

def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]

        person = Person.objects.create(
            name=name,
            age=age
        )
        person.save()
        messages.success(request,"Successfuly Save")

        return redirect("/")
    
    else:
        return render(request,"form.html")
    
def edit(request,person_id):
    person = Person.objects.get(id=person_id)
    if request.method == "POST":
        person.name = request.POST["name"]
        person.age = request.POST["age"]
        person.save()
        messages.success(request,"Successfuly Update")

        return redirect("/")
    else:
        return render(request,"edit.html",{"person":person})
    
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.error(request,"Successfuly Delete")

    return redirect("/")