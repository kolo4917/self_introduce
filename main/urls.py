from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('page1/', views.page1_view, name='page1'),
    path('page2/', views.page2_view, name='page2'),
    path('page4/', views.page4_view, name='page4'),
    path('page5/', views.page5_view, name='page5'),

]

