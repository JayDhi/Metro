# App/Route/views.py
# import from framework
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
# import from project
from .models import Route
from .serializers import ShowRoute, EditRoute

@api_view(['GET'])
def get_route(request):
    if "route" in request.data:
        slzr = ShowRoute(Route.objects.filter(
                                    route_id__in=request.data["route"]), 
                                        many=True)
    else:
        slzr = ShowRoute(Route.objects.all(), many=True)
    return JsonResponse(data=slzr.data, safe=False)


# input format
# {"route_info": {"route_name"}, "relationship":{}}
@api_view(['POST'])
def edit_route(request):
    data = request.data["route_info"]
    context = request.data["relationship"]
    try:
        route = Route.objects.get(route_name=data["route_name"])
    except KeyError:
        return JsonResponse(data={"errors": "Check Json Parameter"})
    except Route.DoesNotExist:
        slzr = EditRoute(data=data, context=context)
    else:
        slzr = EditRoute(route, data=data, context=context)
    if slzr.is_valid():
        slzr.save()
        return JsonResponse(data=slzr.data, safe=False)
    else:
        return JsonResponse(slzr.errors)