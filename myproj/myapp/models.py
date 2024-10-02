from django.db import models

# Create your models here.


class product(models.Model):
  name = models.CharField(max_length=200, verbose_name="Наименование")
  count = models.IntegerField(verbose_name="Кол-во")
  cost = models.IntegerField(verbose_name="Стоимость")
  dot = models.DateTimeField(auto_now=True, verbose_name="Дата")
  pct = models.ImageField(upload_to="myapp/static/img", blank=True)

  def __str__(self):
    return self.name
  
  



class Animal(models.Model):
    name = models.CharField(max_length=100)
    sound = models.CharField(max_length=100)

    def speak(self,a,b):
      #return f'The {self.name} says "{self.sound}"'
      return a+b