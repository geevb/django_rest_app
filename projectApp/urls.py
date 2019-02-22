from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework import routers
from srCurriculos.controllers import ResumesAPI
from srCurriculos import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^resumes/', ResumesAPI.as_view(), name='resumes'),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'admin/', admin.site.urls),
    url(r'authentication/', include('srCurriculos.urls')),
]