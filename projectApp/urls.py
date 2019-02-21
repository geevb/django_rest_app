from django.conf.urls import url
from rest_framework.authtoken import views as rest_framework_views
from django.conf.urls import url
from rest_framework import routers
from srCurriculos.views import ResumesAPI

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^resumes/', ResumesAPI.as_view(), name='resumes')
]