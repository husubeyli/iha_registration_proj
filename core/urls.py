from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('iha/create/', views.IHACreateView.as_view(), name='iha_create'),
    path('iha/list/', views.IHAListView.as_view(), name='iha_list'),
    path('iha/<slug:slug>/detail/', views.IHADetailView.as_view(), name='iha_detail'),
    path('iha/<int:pk>/delete/', views.IHADeleteView.as_view(), name='iha_delete'),    
    path('iha/<slug:slug>/update/', views.IHAUpdateView.as_view(), name='iha_update')
]