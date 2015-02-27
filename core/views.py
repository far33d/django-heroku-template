from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from cokitchen.stripe_settings import stripe

from core.models import TestItem, PurchaseRecord

# Create your views here.

def index(request):
    items = TestItem.objects.order_by('price')
    context = {'items': items}
    return render(request, 'core/index.jinja', context)

@csrf_exempt
def purchase(request, item_id):

    post_data = request.POST
    token_id = post_data['id']
    customer_email = post_data['email']

    item = TestItem.objects.get(pk=item_id)

    stripe.Token.retrieve(token_id)

    charge = stripe.Charge.create(
      amount=item.price_cents(),
      currency='usd',
      source=token_id,
      description='purchase of %s for %s' % (item.name, customer_email)
    )

    purchase_record = PurchaseRecord(item=item)
    purchase_record.customer_email = customer_email
    purchase_record.stripe_token = token_id

    purchase_record.save()

    return HttpResponse(':)')
