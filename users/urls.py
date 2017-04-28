from django.conf.urls import include, url
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.views import password_reset, password_reset_confirm, password_reset_done, login, logout


from users.views import *

urlpatterns = [
	url(r'^signup/$', UserCreateView.as_view(), name='signup'),
	url(r'^confirm/(?P<user_id>\d+)/$', SendConfirmationView.as_view(), name='send_confirmation'),
	url(r'^confirm/(?P<user_id>\d+)/(?P<token>.+)/$', CheckConfirmationView.as_view(), name='check_confirmation'),

	url(r'^update/(?P<user_id>\d+)/$', UserUpdateView.as_view(), name='user_update'),

	url(r'^password/reset/$', password_reset, {'template_name' : 'users/password_reset.html',
											'post_reset_redirect' : reverse_lazy('password_reset_sent')},
											name='password_reset'),

	url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)/(?P<token>.+)/$', password_reset_confirm,
														{'template_name' : 'users/password_reset_confirm.html',
														'post_reset_redirect' : reverse_lazy('login')},
														name='password_reset_confirm'),

	url(r'^password/reset/sent/$', password_reset_done, { 'template_name' : 'users/password_reset_sent.html',},
														name='password_reset_sent'),

	url(r'^login/$', login, {'template_name' : 'users/login.html'}, name='login'),
	url(r'^logout/$', logout ,{'next_page' : reverse_lazy('login')}, name='logout'),
]
