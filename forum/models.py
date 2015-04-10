from django.db import models
from django.contrib.auth.models import User

# Create your models here. 


class Teacher(models.Model):
	name = models.CharField(max_length = 200)
	classrooms = models.ManyToManyField('Classroom')
	user = models.OneToOneField(User)

class Student(models.Model):
	name = models.CharField(max_length = 200)
	classrooms = models.ManyToManyField('Classroom')
	user = models.OneToOneField(User)

class Classroom(models.Model):
	class_name = models.CharField(max_length = 200)
	teachers = models.ManyToManyField('Teacher')
	students = models.ManyToManyField('Student')

class Question(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField(max_length = 1000, default = '')
	author = models.ForeignKey('Student')

class Note(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey('Teacher')

class Comment(models.Model):
	text = models.TextField(max_length = 1000, default = '')
	author = models.ForeignKey('Student')

class Answer(models.Model):
	author = models.ForeignKey('Teacher')
	text = models.TextField(max_length = 1000, default = '')

