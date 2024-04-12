from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('book', views.BooksViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('get_books/', views.BooksView.as_view(), name='get_books'),
    path('settings/', views.UserSettings.as_view(), name='settings')
]
