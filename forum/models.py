from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    TEACHER, STUDENT = range(2)
    TYPE_CHOICES = [(TEACHER, "Teacher"), (STUDENT, "Student")]

    user = models.OneToOneField(User)
    type = models.IntegerField(choices = TYPE_CHOICES, default = STUDENT)
    classrooms = models.ManyToManyField('Classroom')


class Classroom(models.Model):
    class_name = models.CharField(max_length = 200)
    class_id = models.IntegerField()

    def __unicode__(self):
        return self.class_name


class Post(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField(max_length = 1000, default = '')
    author = models.ForeignKey('Profile')
    classroom = models.ForeignKey('Classroom', null = True)

    def __unicode__(self):
        return self.title

    def author(self):
        return self.author
