from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^classes/$', views.classes, name='class_list'),
    url(r'^classes/(?P<class_id>[0-9]+)/$', views.classroom, name='classroom'),
    url(r'^register/$', views.register, name='register'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^profile_update_form/$', views.RegisterforClasses.as_view(), name='register_for_classes'),
    url(r'^(?P<pk>\d+)/post_update_form/$', views.EditPost.as_view(), name='edit_post'),
]