from django.shortcuts import render, redirect
from testapp_dcod.models import Data_piece
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def index(request):
    # View for start template
    data = Data_piece.objects.all()
    # Take regions for select button
    regions = []
    for things in data:
        if things.region in regions:
            pass
        else:
            regions.append(things.region)
        
    return render(request, 'testapp_dcod/index.html', {'data' : data, 'regions' : regions})

def findcountryview(request):
    #View for obtain data from db. Need for build graphics
    if request.method == 'GET':
        region = request.GET.get('inputregion')
        try:
            victims = Data_piece.objects.filter(region=region).values('country', 'number')

            return JsonResponse({'results': list(victims)})

        except:
            json_data = 'No region'

            return HttpResponse(json_data)