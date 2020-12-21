from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
	path('<int:question_id>/vote/', views.vote, name = 'vote'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/', views.detail, name = 'detail'),
	path("", views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


