from django.urls import path

from .views import SignUpView, UpdateInfoView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update/', SignUpView.as_view(), name='update_info'),
]
