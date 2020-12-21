from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .GCBPS.carprices import getPricesEx
from .GCBPS.prayers import praytime as namaz
from .GCBPS.carstats import oldcarprice, oldcargems, caravgs
# Create your views here.


def xcar(request):
    data = {
        'name': 'XCar App',
        'author': 'three6tdegree@gmail.com',
        'desc': 'This App provides higher level interface to GCBPS scripts',
        'examples': {
            'car suggestions': 'http://192.168.100.16:8000/xcars/cargemshtml/mk_honda%7Cmd_civic%7Cyr_2017_2017',
            'prayers timing': 'http://192.168.100.16:8000/xcars/praytime/',
            'car average asking price': 'http://192.168.100.16:8000/xcars/carstat/mk_chevrolet|md_optra',
            'list car average asking price by range': 'http://192.168.100.16:8000/xcars/caravgs/mk_chevrolet|md_joy|yr_2005_2012',
        }
    }
    return JsonResponse(data, safe=False)


def pricelist(request, brand):
    data = getPricesEx(brand)
    return JsonResponse(data, safe=False)


def praytime(request):
    data = namaz(False)
    return JsonResponse(data, safe=False)


def gemht(data):
    list = data[1]
    ht = ""
    for item in list:
        url = item[0]
        img = item[1]
        cost = item[2]
        ht += "<a href='" + url + "'><img src='"+img+"'>"+cost+"</a><hr>"
    return ht


def avgsht(data):
    ht = ''
    for item in data:
        ht += str(item[0]).replace("mk_", '').replace("/md_",
                                                      " ").replace("/yr_", ' ')[:-5].title()+'\t'+item[1]+'<br/>'
    return ht


def caravgshtml(request, spec):
    if 'mk_' in spec and 'md_' in spec and 'yr_' in spec:
        data = caravgs(spec)
        return HttpResponse(avgsht(data))
    else:
        return JsonResponse(['error :carstat', 'requires minimum make (mk_) and model (md_) and (yr_)from_to'], safe=False)


def cargemshtml(request, spec):
    if 'mk_' in spec and 'md_' in spec:
        data = oldcargems(spec)
        return HttpResponse(gemht(data))
    else:
        return JsonResponse(['error :carstat', 'requires minimum both make (mk_) and model (md_)'], safe=False)


def cargems(request, spec):
    if 'mk_' in spec and 'md_' in spec:
        data = oldcargems(spec)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse(['error :carstat', 'requires minimum both make (mk_) and model (md_)'], safe=False)


def carstat(request, spec):
    if 'mk_' in spec and 'md_' in spec:
        data = oldcarprice(spec)
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse(['error :carstat', 'requires minimum both make (mk_) and model (md_)'], safe=False)
