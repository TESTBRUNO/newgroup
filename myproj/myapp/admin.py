from django.contrib import admin

from myapp.models import product

class myconfigprod(admin.ModelAdmin):

  list_display = ["name","count","cost","dot"]

admin.site.register(product,myconfigprod)

# Register your models here.

# python manage.py shell
# new = product(name = "Пылесос ручной",count = "300",  cost= "31990")
# new.save()

#python manage.py makemigrations – создание миграции
#python manage.py  sqlmigrate myapp 0001 – просмотр sql #запроса, который выполнится при миграции 
#python manage.py  migrate – применить изменения для базы #данных

# python manage.py createsuperuser