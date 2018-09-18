from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from itertools import chain
import datetime

from invoice.models import Customer, Invoice, InvoiceItem


# Accounting report
@login_required(login_url='users:login')
def accounting(request):
    if request.method == 'POST':
        start = datetime.datetime.strptime(request.POST['start'], "%m/%d/%Y")
        end = datetime.datetime.strptime(request.POST['end'], "%m/%d/%Y")

        if start > end:
            context = {
                'error_message' : "Start date must be before end date!",
            }
            return render(request, 'invoice/accounting.html', context)
        else:
            paid_invoices = Invoice.objects.filter(date__gt=start).filter(date__lt=end).filter(status = 'Paid')
            all_invoices = Invoice.objects.filter(date__gt=start).filter(date__lt=end)
            expenses = Expense.objects.filter(date__gt=start).filter(date__lt=end)

            # Sum of all paid invoices
            invoice_total = 0
            for i in paid_invoices:
                invoice_total += i.total_items()

            # Add invoice expenses within date range, regardless of invoice status
            for i in all_invoices:
                expenses = list(chain(expenses, Expense.objects.filter(invoice=i)))

            # Sum of all expenses
            expense_total = 0
            for expense in expenses:
                expense_total += expense.total()

            context = {
                'start': start,
                'end': end,
                'invoices': paid_invoices,
                'expenses': expenses,
                'invoicetotal': invoice_total,
                'expensetotal': expense_total,
                'nettotal': invoice_total - expense_total,
            }
            return render(request, 'invoice/accounting.html', context)
    else:
        return render(request, 'invoice/accounting.html')