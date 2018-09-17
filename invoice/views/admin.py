from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
import datetime

from invoice.models import Customer, Invoice, InvoiceItem



# Administrative settings
def users(request):
    return None


def settings(request):
    return None
