from django.conf.urls import url

from users.views.login_view import sign_in
from users.views.logout_view import sign_out
from users.views.registration_view import registration

urlpatterns = [
    url(r'^registration/$', registration, name="registration"),
    url(r'^$', sign_in, name="login"),
    url(r'^logout/$', sign_out, name="logout"),
]
