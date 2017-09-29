from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^$', views.index),
	url(r'^(?P<slug>[\w\-]+)/$',views.post,),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),]