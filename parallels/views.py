from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def frmbtnsubmit():
    return "<br><input type='submit' id='btnsubmit' name='btnsubmit'><br>"


def frminp(tag, label):
    return "<label for='"+tag+"'>"+label+"</label><br><input type='text' id='"+tag+"' name='"+tag+"'><br>"


def index(request):
    resp = HttpResponse()
    resp.write(
        "<p>Please Select the Car for which you would like to see Analytics.</p>")
    resp.write("<form>")
    resp.write(frminp('carmake', 'Car Make:'))
    resp.write(frminp('carmodel', 'Model:'))
    resp.write(frminp('year', 'Year:'))
    resp.write(frmbtnsubmit())
    resp.write("</form>")
    return resp
