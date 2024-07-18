from django.urls import path

from measurement.views import ListCreateSensorsView, \
    ListUpdateSensorView, MeasurementCreateSerializerView

urlpatterns = [
    path('sensors/', ListCreateSensorsView.as_view()),
    path('sensors/<pk>', ListUpdateSensorView.as_view()),
    path('measuriments/', MeasurementCreateSerializerView.as_view()),

]
