from django.conf.urls import url

from users.views import registration, sign_in, sign_out

urlpatterns = [

    url(r'^registration/$', registration, name="registration"),

    url(r'^$', sign_in, name="login"),
    url(r'^logout/$', sign_out, name="logout"),

    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^login/$', sign_in, name="login"),
    url(r'^logout/$', sign_out, name="logout"),

]