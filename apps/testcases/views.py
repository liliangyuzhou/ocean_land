
from rest_framework import viewsets,permissions,decorators
from rest_framework.response import Response
from . import serializer
from apps.testcases.models import Testcases
class TestCasesViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.TestCaseModelSerializer
    queryset = Testcases.objects.filter(is_delete=False)