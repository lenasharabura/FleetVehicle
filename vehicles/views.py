from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer
from rest_framework.response import Response


class VehicleListView(ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers == 'no':
            print('test')
            return queryset.filter(driver_id__isnull=True)
        if with_drivers == 'yes':
            print('yes')
            return queryset.filter(driver_id__isnull=False)

        return queryset


class VehicleDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_url_kwarg = 'vehicle_id'


class SetDriverView(UpdateAPIView):

    def post(self, **kwargs):
        vehicle_id = self.kwargs['vehicle_id']
        driver_id = self.kwargs['driver_id']
        vehicles = Vehicle.objects.all()
        vehicles.filter(id=vehicle_id).update(driver_id=driver_id)
        return Response()


class DeleteDriverView(UpdateAPIView):

    def post(self, **kwargs):
        vehicle_id = self.kwargs['vehicle_id']
        vehicles = Vehicle.objects.all()
        vehicles.filter(id=vehicle_id).update(driver_id=None)
        return Response()

