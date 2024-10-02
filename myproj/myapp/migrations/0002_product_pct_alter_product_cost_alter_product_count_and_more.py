# Generated by Django 4.2.5 on 2024-09-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pct',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.IntegerField(verbose_name='Кол-во'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dot',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
    ]
