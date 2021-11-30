from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import decorators
from .serializer import EnvModelSerializer,EnvNameSerializer
from .models import Envs
from utils.tools import env_time_format

class EnvsViewSet(ModelViewSet):
    serializer_class = EnvModelSerializer
    queryset = Envs.objects.filter(is_delete=False)

    def perform_destroy(self, instance):
        instance.is_delete=True
        instance.save()


    def get_serializer_class(self):
        if self.action=='names':
            return EnvNameSerializer
        else:
            return self.serializer_class

    @decorators.action(detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)

    def list(self, request, *args, **kwargs):
        response=super(EnvsViewSet, self).list(request, *args, **kwargs)
        response.data['results']=env_time_format(response.data['results'])
        return response