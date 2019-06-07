from django.conf.urls import include, url
from django.urls import reverse_lazy

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, LoginView, LogoutView


from users.views import *

urlpatterns = [
	url(r'^signup/$', UserCreateView.as_view(), name='signup'),
	url(r'^confirm/(?P<user_id>\d+)/$', SendConfirmationView.as_view(), name='send_confirmation'),
	url(r'^confirm/(?P<user_id>\d+)/(?P<token>.+)/$', CheckConfirmationView.as_view(), name='check_confirmation'),

	url(r'^update/(?P<user_id>\d+)/$', UserUpdateView.as_view(), name='user_update'),

	url(r'^password/reset/$', PasswordResetView.as_view(**{'template_name' : 'users/password_reset.html',
											'success_url' : reverse_lazy('password_reset_sent')}),
											name='password_reset'),

	url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(
											                        **{'template_name' : 'users/password_reset_confirm.html',
														'success_url' : reverse_lazy('login')}),
														name='password_reset_confirm'),

	url(r'^password/reset/sent/$', PasswordResetDoneView.as_view(**{ 'template_name' : 'users/password_reset_sent.html',}),
														name='password_reset_sent'),

	url(r'^login/$', LoginView.as_view(**{'template_name' : 'users/login.html'}), name='login'),
	url(r'^logout/$', LogoutView.as_view(**{'next_page' : reverse_lazy('login')}), name='logout')
]
