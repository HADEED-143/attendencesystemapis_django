from django.shortcuts import render

# Create your views here.
def home(request):
   .objects.all()

    .objects.all()

         =Orders.count()

    delivered = .flter(status='').count()

    pending = .filter(status='').count()

    context = {}

    return render(request, 'Templates/dashboard.html', context)

def userpanel(request):

    .objects.all()
    return render(request, 'Templates/', {})

def adminpanel(request, pk_test):

    .objects.get(id=pk_test)

    .order_set.all()

    context = {}

    return render(request, 'Templates', context)

"""
def createOrder(requet):
    form = OrderForm()

    context = {'form':form}

    return render(request, 'api/order_form.html', context)

"""