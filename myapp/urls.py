from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('find-job/', views.find_job, name='find_job'),
    path('hire-talent/', views.hire_talent, name='hire_talent'),
]
