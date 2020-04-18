from . import views
from django.urls import path




urlpatterns = [
    path('',views.UserView.as_view(),name='api'),
    path('api/',views.UserView.as_view(),name='api'),
    path('api/<int:pk>/',views.Detail_Views.as_view(),name='api_detail'),
    path('api/<int:pk>/update/',views.Detail_Views.as_view(),name='api_update'),
]
