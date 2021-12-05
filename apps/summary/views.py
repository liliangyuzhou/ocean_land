from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.db.models import Sum
from projects.models import Projects
from testsuites.models import TestSuites
from interfaces.models import Interfaces
from apps.testcases.models import Testcases
from envs.models import Envs
from configures.models import Configures
from apps.debugtalk.models import DebugTalks
from reports.models import Reports


class SummaryApiView(APIView):
    def get(self, request):
        """
        统计信息，只有一个查询接口，就不选用查询集viesets
        :param request:
        :return:
        """
        user = request.user
        user_info = {
            'username': user.username,
            'role': '管理员' if user.is_superuser else '普通用户',
            'date_joined': datetime.strftime(user.date_joined, "%Y-%m-%d %H:%M:%S") if user.date_joined else '',
            'last_login': datetime.strftime(user.last_login, "%Y-%m-%d %H:%M:%S") if user.last_login else '',
        }

        projects_count = Projects.objects.filter(is_delete=False).count()
        testcases_count = Testcases.objects.filter(is_delete=False).count()
        interfaces_count = Interfaces.objects.filter(is_delete=False).count()
        testsuites_count = TestSuites.objects.filter(is_delete=False).count()
        debug_talks_count = DebugTalks.objects.filter(is_delete=False).count()
        envs_count = Envs.objects.filter(is_delete=False).count()
        configures_count = Configures.objects.filter(is_delete=False).count()
        reports_count = Reports.objects.filter(is_delete=False).count()
        # Reports.objects.filter(is_delete=False).aggregate(Sum('success'))返回一个字典
        run_testcases_success_count = Reports.objects.filter(is_delete=False).aggregate(Sum('success'))[
                                          'success__sum'] or 0
        run_testcases_count = Reports.objects.filter(is_delete=False).aggregate(Sum('count'))['count__sum'] or 0
        if run_testcases_count:
            success_rate = int((run_testcases_success_count / run_testcases_count) * 100)
            fail_rate = 100 - success_rate
        else:
            success_rate = 0
            fail_rate = 0
        stat_list = {
            'projects_count': projects_count,
            'interfaces_count': interfaces_count,
            'testcases_count': testcases_count,
            'testsuites_count': testsuites_count,
            'debug_talks_count': debug_talks_count,
            'envs_count': envs_count,
            'configures_count': configures_count,
            'reports_count': reports_count,
            # 'run_testcases_success_count':run_testcases_success_count,
            # 'run_testcases_count':run_testcases_count,
            'success_rate': success_rate,
            'fail_rate': fail_rate,
        }
        return Response(data={'stat_list':stat_list,'user':user_info}, status=status.HTTP_200_OK)
