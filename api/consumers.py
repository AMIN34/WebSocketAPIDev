from .models import SensorData
from .serializers import SensorDataSerializer

from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework import permissions

class SensorDataConsumer(GenericAsyncAPIConsumer):
    queryset = SensorData.objects.all()
    permission_classes = (permissions.AllowAny)
    
    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        await super().connect()
        
    @model_observer(SensorData)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)
    
    @model_change.serialize
    def model_serialize(self, instance, action, **kawrgs):
        return dict(data=SensorDataSerializer(instance=instance).data, action=action.value)