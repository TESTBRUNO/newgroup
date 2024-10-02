from django.shortcuts import render, redirect
from myapp.models import product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.

def index(request):
  if request.method == "POST":
    data = request.POST
    print(data)
    new = product(name = data["field1"], count = data["field2"], cost = data["field3"])
    new.save()
  return render(request,"index.html")



def card(request):
  if request.session.get("is_auth", False):
    data = product.objects.all()
    new_user = User.objects.filter(id = request.session.get("user", 0))
    return render(request,"card.html", {"res":data, "user":new_user})
  else:
    return redirect(user_auth)



def user_reg(request):
  if request.method == "POST":
    data = request.POST
    user = User.objects.create_user(data["field1"], data["field2"], data["field3"])
    user.save()
  return render(request,"index.html")





def user_auth(request):
   if request.method == "POST":
      data = request.POST
      user = authenticate(username = data["field1"], password = data["field2"])
      if user is not None:
        request.session["is_auth"] = True
        request.session["user"] = user.id
        return redirect(card)

      else:
        return HttpResponse("Ошибка")
   else:
    return render(request,"index.html",{})



#В CMD
#python -m venv env
#env\Scripts\activate 
#Вернутся в папку с проектом и #выполнить установку(..\) Django
#Pip install Django (нужно проверить, #что мы находимся в нашем виртуальном #окружении)
#Pip freeze (проверка установки #пакета)

#Django-admin – список доступных #команд
#django-admin startproject mysite – #создание проекта
# python manage.py startapp
#Python manage.py runserver

