from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def frmbtnsubmit():
    return "<br><input type='submit' id='btnsubmit' name='btnsubmit'><br>"


def frminp(tag, label):
    return "<label for='"+tag+"'>"+label+"</label><br><input type='text' id='"+tag+"' name='"+tag+"'><br>"


def processMakeModelYear(mk, md, yr):
    data = [
        {'make': mk, 'model': md, 'year': yr},
        {'name': 'Julia', 'email': 'julia@example.org'}
    ]
    return data


def index(request):
    carmake = ""
    carmodel = ""
    caryear = ""
    resp = HttpResponse()
    try:
        carmake = request.GET['carmake']
        carmodel = request.GET['carmodel']
        caryear = request.GET['caryear']
        return JsonResponse(processMakeModelYear(carmake, carmodel, caryear), safe=False)
    except:
        resp.write(
            "<p>Please Select the Car for which you would like to see Analytics.</p>")
        resp.write("<form>")
        resp.write(frminp('carmake', 'Car Make:'))
        resp.write(frminp('carmodel', 'Model:'))
        resp.write(frminp('caryear', 'Year:'))
        resp.write(frmbtnsubmit())
        resp.write("</form>")
    return resp
