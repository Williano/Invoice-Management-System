import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from invoice.models import Customer, Invoice, InvoiceItem
from invoice.models.customer import Customer
from invoice.models.inv import Invoice


@login_required(login_url='users:login')
def customer_list(request):
    """List all Customers

    List all customers and paginate them to display 25
    customers per page.

    """
    customer = Customer.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(customer, 25)
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        customers = paginator.page(paginator.num_pages)
    context = {
        'title' : 'Customer List',
        'customers' : customers,
    }
    return render(request, 'invoice/customers.html', context)


@login_required(login_url='users:login')
def customer(request, customer_id):
    """
      Displays the details for a particular customer with their
      invocies.

    """
    customer = get_object_or_404(Customer, pk=customer_id)
    invoices = Invoice.objects.filter(customer = customer).order_by('-date_created')
    context = {
        'title' : "Customer info - %s" % customer.name,
        'customer' : customer,
        'invoices' : invoices,
    }
    return render(request, 'invoice/customer.html', context)


# Add new customer
@login_required(login_url='users:login')
def new_customer(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            name = request.POST['name']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            city = request.POST['city']
            state = request.POST['state']
            zip = request.POST['zip']
            email = request.POST['email']
            # Stuff from form
            c = Customer(name=name, address1=address1, address2=address2,
                         city=city, state=state, zip=zip, email=email)
            c.save()

        if 'savecreate' in request.POST:
            expiration_date = request.POST.get('expiration_date', datetime.date.today())
            status = request.POST.get('status', 'Upaid')
            i = Invoice(customer=c, expiration_date=expiration_date, status=status)
            i.save()
            messages.success(request, 'New Customer successfully created! ')
            return HttpResponseRedirect(reverse('invoice:invoice', args=(i.id,)))
        else:
            return HttpResponseRedirect(reverse('invoice:customer_list'))
    else:
        return render(request, 'invoice/new_customer.html')


# Update customer
@login_required(login_url='users:login')
def update_customer(request, customer_id):
    # Stuff from form
    c = get_object_or_404(Customer, pk=customer_id)

    c.name = request.POST['name']
    c.address1 = request.POST['address1']
    c.address2 = request.POST['address2']
    c.city = request.POST['city']
    c.state = request.POST['state']
    c.zip = request.POST['zip']
    c.email = request.POST['email']

    c.save()
    messages.success(request, 'Customer Details Updated Successfully')

    return HttpResponseRedirect(reverse('invoice:customer', args=(c.id,)))


# Delete customer
@login_required(login_url='users:login')
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return HttpResponseRedirect(reverse('invoice:customer_list'))
