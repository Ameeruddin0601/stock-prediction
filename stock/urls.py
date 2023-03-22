from django.urls import path
from . import views


urlpatterns = [
    path('', views.stock, name='stock'),
    path('analysis/', views.analysis, name='analysis'),
    path('analysis1/', views.analysis1, name='analysis1'),

    # path('success/', views.success_page, name='success_page'),
]
