from django.urls import path

from srcurriculos.users import views

urlpatterns = [
    path('register/', views.register)
]