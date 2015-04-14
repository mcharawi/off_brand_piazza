from django import forms
from .models import Profile, Post, Classroom
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


class PostForm(forms.ModelForm):
	title = forms.CharField(max_length = 200)
	text = forms.CharField(widget=forms.Textarea)
	classroom = forms.ModelChoiceField(queryset=Classroom.objects.all())	

	class Meta:
		model = Post
		fields = ('title', 'text', 'classroom')