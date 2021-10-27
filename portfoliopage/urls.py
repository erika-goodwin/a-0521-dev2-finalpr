from django.urls import path
from portfoliopage import views

urlpatterns = [



    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('snowboarding/', views.snowboarding, name='snowboarding'),
    path('traveling/', views.traveling, name='traveling'),

    
    
]
