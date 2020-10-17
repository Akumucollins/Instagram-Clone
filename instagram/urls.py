from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'instagram'
urlpatterns = [
    path('', views.home,name='home'),
]
if settings.DEBUG:
    urlpatterns+= static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
if settings.DEBUG:
    urlpatterns+= static(
        settings.STATIC_URL, 
        document_root = settings.STATIC_ROOT)    