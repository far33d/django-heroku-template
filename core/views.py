from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from core.models import TestItem, PurchaseRecord

# Create your views here.

def index(request):
    items = TestItem.objects.order_by('price')
    context = {'items': items}
    return render(request, 'core/index.jinja', context)

@csrf_exempt
def purchase(request, item_id):

    post_data = request.POST

    item = TestItem.objects.get(pk=item_id)
    purchase_record = PurchaseRecord(item=item).save()

    return HttpResponse(':)')
