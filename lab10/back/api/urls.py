from django.urls import path
from . import views
from rest_framework import routers

r = routers.SimpleRouter()

r.register(r'company', views.CompanyModelViewSet)
r.register(r'vacancy', views.VacanciesModelViewSet)

urlpatterns = r.urls