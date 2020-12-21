from django.urls import path

from . import views

urlpatterns = [
    path('', views.xcar, name='xcars'),
    path('pricelist/<str:brand>', views.pricelist, name='pricelist'),
    path('praytime/', views.praytime, name='praytime'),
    path('carstat/<str:spec>', views.carstat, name='carstat'),
    path('cargems/<str:spec>', views.cargems, name='cargems'),
    path('cargemshtml/<str:spec>', views.cargemshtml, name='cargemshtml'),
    path('caravgs/<str:spec>', views.caravgshtml, name='caravgshtml'),
]
