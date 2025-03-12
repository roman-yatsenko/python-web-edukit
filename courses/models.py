from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Спеціалізація"
        verbose_name_plural = "Спеціалізації"
        ordering = ['title']
    
    def __str__(self):
        return self.title
    

class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE, verbose_name="Викладач")
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE, verbose_name="Спеціалізація")
    title = models.CharField(max_length=200, verbose_name="Назва")
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(verbose_name="Опис")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курси"
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE, verbose_name="курс")
    title = models.CharField(max_length=500, verbose_name="Назва")
    description = models.TextField(blank=True) 

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Теми"

    def __str__(self):
        return self.title
    