from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product
from order.models import order
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum

# Create your views here.

@login_required(login_url="/accounts/login/")
def posview(request):
    if request.method == 'POST':
        # Page from the theme
        product_list = product.objects.all()
        coffee = request.POST.items()
        o_id = int(datetime.now().timestamp())
        for x in list(product_list.values('id')):
            if request.POST[str(x['id']) + "_qnt"] != "":
                qnt = int(request.POST[str(x['id']) + "_qnt"])
                ord = order()
                ord.order_id = o_id
                ord.product = product.objects.get(pk=int(x['id']))
                price = product.objects.get(pk=int(x['id'])).price
                ord.total = price * qnt
                ord.type = "POS"
                ord.quantity = qnt
                ord.save()

        return redirect("pos")

    else:
        # Page from the theme
        product_list = product.objects.all()
        latest_order = order.objects.latest('created_at').order_id
        last_order = order.objects.filter(order_id=latest_order)
        cart_value = last_order.values('order_id').annotate(sum=Sum('total'))[0]['sum']
        context = {
            'products':product_list,
            'product_list' : list(product_list.values('id', 'price')),
            'latest_order':last_order,
            'cart_value':cart_value,
        }

        return render(request, 'pages/pos-page.html', context)
