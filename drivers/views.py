from datetime import datetime
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from drivers.models import Driver
from drivers.serializers import DriverSerializer


class DriverListView(ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get_queryset(self):
        queryset = Driver.objects.all()
        created_at__gte = self.request.query_params.get('created_at__gte')
        if created_at__gte:
            date = datetime.strptime(created_at__gte, "%d-%m-%Y").date()
            return queryset.filter(created_at__gte=date)
        created_at__lte = self.request.query_params.get('created_at__lte')
        if created_at__lte:
            date = datetime.strptime(created_at__lte, "%d-%m-%Y").date()
            return queryset.filter(created_at__lte=date)
        return queryset


class DriverDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    lookup_url_kwarg = 'driver_id'
