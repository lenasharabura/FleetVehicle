
from django.contrib import admin
from django.urls import path

from drivers.views import DriverListView, DriverDetailView
from vehicles.views import VehicleListView, VehicleDetailView, SetDriverView, DeleteDriverView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers/driver/<int:driver_id>/', DriverDetailView.as_view(), name='driver_detail'),
    path('drivers/driver/', DriverListView.as_view(), name='drivers_list'),
    path('vehicles/vehicle/<int:vehicle_id>/', VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicles/vehicle/', VehicleListView.as_view(), name='vehicles_list'),
    path('vehicles/set_driver/<int:vehicle_id>/<int:driver_id>/', SetDriverView.as_view(), name='set_driver'),
    path('vehicles/set_driver/<int:vehicle_id>/', DeleteDriverView.as_view(), name='delete_driver'),
]
