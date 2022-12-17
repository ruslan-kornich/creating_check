from rest_framework.generics import CreateAPIView, ListAPIView, GenericAPIView

from .models import Check
from .serializers import CreateChecksSerializer, ChecksSerializer


class CreateChecksAPIView(CreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CreateChecksSerializer


class ListChecksAPIView(ListAPIView):
    queryset = Check.objects.all()
    serializer_class = ChecksSerializer


class PDFChecksAPIView(GenericAPIView):
    queryset = Check.objects.all()
    serializer_class = ChecksSerializer
