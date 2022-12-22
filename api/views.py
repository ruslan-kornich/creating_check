from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Check, Printer
from .serializers import OrderSerializer
from .services import create_checks


class OrdersAPIView(APIView):
    """Клас генерації pdf-файлів чеків для клієнтів та для кухні."""

    def post(self, format=None):
        order = OrderSerializer(data=self.request.data)
        order.is_valid(raise_exception=True)
        order = order.data
        checks = Check.objects.filter(order=order)
        if checks:
            return Response(
                {
                'error': 'Чеки для цього замовлення були раніше створені'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        printers = Printer.objects.filter(point_id=order['point_id'])
        kitchen_printer = printers.filter(check_type='kitchen').first()
        client_printer = printers.filter(check_type='client').first()
        if not (kitchen_printer and client_printer):
            return Response(
                {'error': 'На цій точці принтери відсутні'},
                status=status.HTTP_400_BAD_REQUEST
            )
        with transaction.atomic():
            kitchen_check = Check.objects.create(
                printer=kitchen_printer,
                type='kitchen',
                order=order,
                status='new',
            )
            client_check = Check.objects.create(
                printer=client_printer,
                type='client',
                order=order,
                status='new'
            )

        if not (kitchen_check and client_check):
            return Response(
                {'error': 'Виникла помилка під час створення чеків'}, status=status.HTTP_400_BAD_REQUEST)

        create_checks(order=order)
        return Response(
            {'OK': 'Чеки успішно створені'}, status=status.HTTP_200_OK
        )
