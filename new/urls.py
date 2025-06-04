from django.urls import path
from .views import forma_view

urlpatterns = [
    path('', forma_view, name='forma'),
]
