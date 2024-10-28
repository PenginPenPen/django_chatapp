from django.urls import path
from .views import chatView,redirect_view


urlpatterns = [
    path('timeline', chatView.as_view(), name='chat'),
    path('',redirect_view,name='redirect')
]