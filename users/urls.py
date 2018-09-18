from django.conf.urls import url

from users.views import registration, sign_in, sign_out

urlpatterns = [

    url(r'^registration/$', registration, name="registration"),
    url(r'^login/$', sign_in, name="login"),
    url(r'^logout/$', sign_out, name="logout"),
]