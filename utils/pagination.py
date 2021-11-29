#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/11 14:27 
# email： liang1.li@ximalaya.com
#自定义的分页类，修改一些默认的属性
from rest_framework.pagination import PageNumberPagination as _PageNumberPagination

class PageNumberPagination(_PageNumberPagination):
    #每页默认的数据条数，优先级最高，比全局配置还要高'PAGE_SIZE': 3,所以全局配置不需要注销
    page_size =10
    #每页查询字符串的名称，默认是'page'，可以更改
    page_query_param = 'page'
    #每页指定数据条数的查询字符串的名称，默认是None，可以修改
    page_size_query_param = 'size'
    page_query_description = '第几页'
    page_size_query_description = '每页几条'
    #每页限制最多展示的数据条数
    max_page_size = 50
    #定义无效页面的页码提示，默认源码是_('Invalid page.')
    invalid_page_message = '页码无效'

    def get_paginated_response(self, data):
        response=super(PageNumberPagination, self).get_paginated_response(data)
        response.data['total_pages']=self.page.paginator.num_pages
        response.data['current_page_num']=self.page.number
        return response

