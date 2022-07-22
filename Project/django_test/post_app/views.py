import json
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from post_app.models import TestPost
from post_app.serializer import TestPostLogSerializer


# 接口函数
# FBV 函数视图
# 最基础
def FBV_post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            username = request.POST.get('username', 0)
            password = request.POST.get('password', 0)
            # 判断参数中是否含有用户名和密码
            if username and password:
                dic['账号'] = username
                dic['密码'] = password
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误！！！')
        else:
            return HttpResponse('输入为空！！！')

    else:
        return HttpResponse('尚未登录！！！')


# 升级版
@api_view(['GET', 'POST'])
def FBV_api_view(request):
    """
    列出所有的TestPost，或者创建一个新的TestPost。
    """
    if request.method == 'GET':
        test_post = TestPost.objects.all()
        serializer = TestPostLogSerializer(test_post, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TestPostLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




