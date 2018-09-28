"""invoicemanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Third party apps.
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

# Local application imports
from .routers import router

urlpatterns = [
    url(r'^', include('users.urls', namespace="users")),
    url(r'^invoice/', include('invoice.urls', namespace="invoice")),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^all_invoices/$',
        TemplateView.as_view(template_name='invoice/vuejs_all_invoices.html'),
        name='vue_all_invoices'),
]
