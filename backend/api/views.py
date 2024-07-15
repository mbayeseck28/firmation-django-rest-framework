from django.http import JsonResponse, HttpResponse
from products.models import Product
from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
import json
# Rest API
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first() 
    data = {}
    if instance:
        # data['id'] = mode_data.id
        # data['title'] = mode_data.title
        # data['content'] = mode_data.content
        # data['titpricele'] = mode_data.price

        # data = model_to_dict(instance, fields=['id', 'title', "price", "sale_price"])
        data = ProductSerializer(instance).data
        # data = dict(data)
        # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})
    # return JsonResponse(data)
    return Response(data)