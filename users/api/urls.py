from django.urls import path, include
from .views import RegisterView, UpdateUserView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('update-profile/<int:pk>', UpdateUserView.as_view()),
]
