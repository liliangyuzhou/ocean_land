from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import decorators
from .serializer import InterfacesSerializer,InterfacesNameSerializer
from .models import Interfaces
from apps.testcases.models import Testcases
from configures.models import Configures
from utils.tools import get_count_by_interface
# Create your views here.

class InterfacesViewSet(viewsets.ModelViewSet):
    serializer_class = InterfacesSerializer
    queryset = Interfaces.objects.filter(is_delete=False)


    def perform_destroy(self, instance):
        instance.is_delete=True
        instance.save()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            datas=serializer.data
            datas=get_count_by_interface(datas)
            return self.get_paginated_response(datas)

        serializer = self.get_serializer(queryset, many=True)
        datas = serializer.data
        datas = get_count_by_interface(datas)
        return Response(datas)

    @decorators.action(detail=False)
    def names(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data, status=200)

    def get_serializer_class(self):
        if self.action=='names':
            return InterfacesNameSerializer
        else:
            return self.serializer_class

    @decorators.action(detail=True)
    def testcases(self,request,pk=None):
        testcases=Testcases.objects.filter(interface_id=pk,is_delete=False)
        one_list=[]
        for item in testcases:
            one_list.append(
                {'id':item['id'],
                 'name':item['name']
                 }
            )
        return Response(data=one_list)

    @decorators.action(detail=True,url_path='configs')
    def configures(self,request,pk=None):
        configures=Configures.objects.filter(interface_id=pk,is_delete=False)
        one_list=[]
        for item in configures:
            one_list.append(
                {'id':item['id'],
                 'name':item['name']
                 }
            )
        return Response(data=one_list)



