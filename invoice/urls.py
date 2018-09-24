from django.conf.urls import url
from . import views

app_name = 'invoicemanager'

urlpatterns = [

    url(r'^$', views.invoices.index, name='index'),

    # INVOICES
    url(r'^invoice/new/$', views.invoices.new_invoice, name='new_invoice'),
    url(r'^invoice/all/$', views.invoices.all_invoices, name='all_invoices'),
    url(r'^invoice/draft/$', views.invoices.draft_invoices, name='draft_invoices'),
    url(r'^invoices/invalid/$', views.invoices.invalid_invoices, name='invalid_invoices'),
    url(r'^invoice/paid/$', views.invoices.paid_invoices, name='paid_invoices'),
    url(r'^invoice/unpaid/$', views.invoices.unpaid_invoices, name='unpaid_invoices'),
    url(r'^invoice/(?P<invoice_id>[0-9]+)/$', views.invoices.invoice, name='invoice'),
    url(r'^invoice/search/$', views.invoices.search_invoice, name='search_invoice'),
    url(r'^view-invoice/(?P<invoice_id>[0-9]+)/$', views.invoices.view_invoice, name='view_invoice'),
    url(r'^invoice/(?P<invoice_id>[0-9]+)/print/$', views.invoices.print_invoice, name='print_invoice'),
    url(r'^invoice/(?P<invoice_id>[0-9]+)/invalidate/$', views.invoices.invalidate_invoice, name='invalidate_invoice'),

    # ITEMS
    url(r'^invoice/(?P<invoice_id>[0-9]+)/item/add/$', views.items.add_item, name='add_item'),
    url(r'^invoice/(?P<invoice_id>[0-9]+)/item/(?P<invoiceitem_id>[0-9]+)/delete/$', views.items.delete_item, name='delete_item'),

    # CUSTOMERS
    url(r'^customers/$', views.customers.customer_list, name='customer_list'),
    url(r'^customer/(?P<customer_id>[0-9]+)/$', views.customers.customer, name='customer'),
    url(r'^customer/(?P<customer_id>[0-9]+)/update/$', views.customers.update_customer, name='update_customer'),
    url(r'^customer/(?P<customer_id>[0-9]+)/delete/$', views.customers.delete_customer, name='delete_customer'),
    url(r'^customer/new/$', views.customers.new_customer, name='new_customer'),
]
