import time
import json

# 获取日志logger
import logging

from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger('ClickStream')


class OpLog_Mid(MiddlewareMixin):
    __exclude_urls = ['index/']  # 定义不需要记录日志的url名单

    def process_request(self, request):
        # 存放请求过来时的时间
        request.init_time = time.time()
        return None

    def process_response(self, request, response):
        # 请求时间
        re_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        # 请求IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # 如果有代理，获取真实IP
            re_ip = x_forwarded_for.split(",")[0]
        else:
            re_ip = request.META.get('REMOTE_ADDR')

        # 请求人
        re_user = request.user.username

        # 请求路径
        re_path = request.path
        # 请求方法
        re_method = request.method

        # 请求参数
        re_content = request.GET if re_method == 'GET' else request.POST
        if re_content:
            # 筛选空参数
            re_content = json.dumps(re_content)
        else:
            re_content = None

        message = '%s %s %s %s %s %s' % (re_time, re_ip, re_user, re_path, re_method, re_content)

        logger.info(message)

        return response

