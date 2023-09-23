from django.shortcuts import render
from django.http import HttpResponse
from order.models import order
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Sum, Q, Count

# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):

    orders_month = order.objects.aggregate(revenue=Sum('total',
            filter=Q(created_at__year=datetime.now().year) &
            Q(created_at__month=datetime.now().month)),
            orders=Count('order_id', filter=Q(created_at__year=datetime.now().year) &
            Q(created_at__month=datetime.now().month), distinct=True))


    context = {
        'orders_month':orders_month,
        'user': request.user.username,
    }

    return render(request, 'pages/custom-index.html',context)
