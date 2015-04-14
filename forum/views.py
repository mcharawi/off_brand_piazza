from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from . import models, forms
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
 
def add_post(request):
	if request.method == 'POST':
		form = forms.PostForm(request.POST)

		if form.is_valid():
			form.save(commit=False)
			form.author = models.Profile.objects.get(user=request.user)
			form.save()
			return index(request)
		else:
			print form.errors
	else:
		form = forms.PostForm()
	return render(request, 'forum/add_post.html', {'form': form})



# Site landing page
def index(request):
	return render(request, 'forum/index.html')

# Login page
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'forum/login.html', {})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/index/')


class RegisterforClasses(UpdateView):
	model = models.Profile
	fields = ['classrooms']
	template_name_suffix = '_update_form'
	success_url = '/index/'

	def get_object(self):
		return models.Profile.objects.get(user=self.request.user)

class EditPost(UpdateView):
	model = models.Post
	fields = ['title', 'text']
	template_name_suffix = '_update_form'
	success_url = '/index/'


# Register page
def register(request):
	registered = False

	if request.method == 'POST':
		user_form = forms.UserForm(data=request.POST)
		profile_form = forms.ProfileForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = forms.UserForm()
		profile_form = forms.ProfileForm()

	return render(request, 'forum/register.html', 
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



# List of classrooms that can be joined
def classes(request):
	if request.user.is_authenticated():
		curr_user = models.Profile.objects.get(user=request.user)
		classroom_list = curr_user.classrooms.all()
		context = RequestContext(request, {'classroom_list': classroom_list,})
	else:
		context = RequestContext(request, {})
	template = loader.get_template('forum/list.html')
	return HttpResponse(template.render(context))


# List of posts for a particular class
def classroom(request, class_id):
	classroom = models.Classroom.objects.get(class_id = class_id)
	posts = models.Post.objects.filter(classroom = classroom)
	template = loader.get_template('forum/class.html')
	context = RequestContext(request, {'posts': posts,})
	return HttpResponse(template.render(context))