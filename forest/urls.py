from django.urls import path
from forest import views

urlpatterns=[
    path('',views.home, name='home'),
    path('tree/',views.trees, name='tree'),
    path('woods_vs_forest/',views.woods_vs_forest, name='wood vs forest')
]