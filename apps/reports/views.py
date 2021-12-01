import json
from datetime import datetime
import os

from django.shortcuts import render

# Create your views here.
import re
from rest_framework import viewsets,permissions,decorators
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from django.utils.encoding import escape_uri_path
from .models import Reports
from .serializer import ReportsModelSerializer
from utils.tools import report_time_format, get_contents_from_file
from ocean_land.settings import REPORT_DIR
class ReportsViewSet(viewsets.ModelViewSet):
    serializer_class = ReportsModelSerializer
    queryset = Reports.objects.filter(is_delete=False)

    def perform_destroy(self, instance):
        instance.is_delete=True
        instance.save()
    def list(self, request, *args, **kwargs):
        response=super(ReportsViewSet, self).list( request, *args, **kwargs)
        response.data['results']=report_time_format(response.data['results'])
        return response
    @decorators.action(detail=True)
    def download(self,request,pk=None):
        instance=self.get_object()
        html=instance.html
        name=instance.name
        name=re.match(r'(.*_)\d+',name)
        if name:
            report_name=name.group(1)+datetime.strftime(datetime.now(),'%Y%m%d%H%M%S')+'.html'
        else:
            report_name=name
        report_path=os.path.join(REPORT_DIR,report_name)
        with open(report_path,'w+',encoding='utf-8') as f:
            f.write(html)

        response=StreamingHttpResponse(get_contents_from_file(report_path))
        report_final_path=escape_uri_path(report_name)
        response['Content-Type']='application/octet-stream'
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(report_final_path)
        return response


    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        datas=serializer.data
        try:
            datas['summary']=json.loads(datas['summary'],encodings='utf-8')
        except Exception as e:
            raise e
        return Response(datas)




