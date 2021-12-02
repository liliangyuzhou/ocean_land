import json

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import ConfigureSerializer
from .models import Configures
from interfaces.models import Interfaces
from utils import handle_data
class ConfigureViewSet(ModelViewSet):
    serializer_class = ConfigureSerializer
    queryset = Configures.objects.filter(is_delete=False)

    def perform_destroy(self, instance):
        instance.is_delete=True
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        config_request=json.loads(instance.request)
        config_header=config_request['config']['request']['headers']
        config_header_list=handle_data.hand_data4(config_header)

        config_variables = config_request['config']['variables']
        config_variables_list=handle_data.hand_data2(config_variables)

        config_name=config_request['config']['name']
        select_interface_id=instance.interface_id

        select_project_id=Interfaces.objects.get(id=select_interface_id).project_id
        response={
            'author':instance.author,
            'config_name':config_name,
            'selected_project_id':select_project_id,
            'selected_interface_id':select_interface_id,
            "header":config_header_list,
            "globalVar":config_variables_list,

        }
        return Response(data=response)