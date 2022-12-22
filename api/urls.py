from django.urls import path

from .views import OrdersAPIView, ChecksAPIView, PDFCheckAPIView

urlpatterns = [
    path('create_checks/', OrdersAPIView.as_view(), name='create_checks'),
    path('new_checks/', ChecksAPIView.as_view(), name='new_checks'),
    path('check/', PDFCheckAPIView.as_view(), name='check'),
]
