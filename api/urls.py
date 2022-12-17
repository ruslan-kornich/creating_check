from django.urls import path

from .views import CreateChecksAPIView, ListChecksAPIView

urlpatterns = [
    path('create_checks/', CreateChecksAPIView.as_view(), name='create_checks'),
    path('list_checks/', ListChecksAPIView.as_view(), name='list_checks'),
]
