# Generated by Django 2.2.3 on 2019-07-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('courses', '0002_remove_course_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o Curso'),
        ),
    ]