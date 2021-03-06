from django.shortcuts import render_to_response
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

def payment_button(request):

    paypal_dict = {
        "business": "aaquibniaz3600@gmail.com",
        "amount": "10",
        "item_name": "bloodtest",
        "invoice": "unique-invoice-00001",
        "notify_url": '127.0.0.1:8000/paypal/',
        "return": '127.0.0.1:8000/paypal-return/',
        "cancel_return": '127.0.0.1:8000/paypal-cancel/',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    return render_to_response('Paypal/payment.html', {"form" : form} )


@csrf_exempt
def paypal_return(request):
    #rgs = {'post': request.POST,'get':request.GET}
    return render_to_response('paypal_cancel.html',{'post': request.POST,'get':request.GET})

@csrf_exempt
def paypal_cancel(request):
    #rgs = {'post': request.POST,'get':request.GET}
    return render_to_response('paypal_cancel.html',{'post': request.POST,'get':request.GET})
