from rest_framework.routers import DefaultRouter
from .views import SensorDataViewSet
router = DefaultRouter()

router.register("sensordata", SensorDataViewSet, basename="sensordata")

urlpatterns = router.urls
