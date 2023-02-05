from django.urls import path

from . import views

app_name = 'infra_app'  # kk

urlpatterns = [
    path('', views.index, name='index'),
    path('second_page/', views.second_page, name='second_page'),

]
