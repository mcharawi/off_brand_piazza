from django import forms
from .models import Profile, Question, Comment, Classroom
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):

	TEACHER, STUDENT = range(2)
	TYPE_CHOICES = [(TEACHER, "Teacher"), (STUDENT, "Student")]
	
	type = forms.ChoiceField(widget=forms.RadioSelect, choices=TYPE_CHOICES)

	class Meta:
		model = Profile
		fields = ('type',)

