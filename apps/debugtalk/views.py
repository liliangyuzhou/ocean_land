from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins

from apps.debugtalk.models import DebugTalks
from .serializer import DebugTalkModelSerializer

class EnvsViewSet(
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = DebugTalkModelSerializer
    queryset = DebugTalks.objects.filter(is_delete=False)

    #这里不重写retrieve，没有办法拿到debugtalk，因为原本retrieve的序列化器中的debugtalk只能反序列化输入，这里
    #需求需要用到debugtalk进行输出，所以这里要我们手动构造

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data_dict={
            'id':instance.id,
            'debugtalk':instance.debugtalk
        }
        return Response(data_dict)
