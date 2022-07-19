from rest_framework import mixins, exceptions, viewsets, status, generics
from django.http import HttpResponse, Http404
import json

# 定义功能
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import ImagesPost
from post.serializer import ImagesPostLogSerializerV2


def add_args(a, b):
    return a + b


# 接口函数 django
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic = {}
        # 判断是否传参
        if request.POST:
            a = request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(a, b)
                dic['number'] = res
                dic = json.dumps(dic)
                return HttpResponse(dic)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')

    else:
        return HttpResponse('方法错误')


# 接口函数 django
# FBV 函数视图
@api_view(['GET', 'POST'])
def images_post_list(request):
    """
    列出所有的snippets，或者创建一个新的snippet。
    """
    if request.method == 'GET':
        images_post = ImagesPost.objects.all()
        serializer = ImagesPostLogSerializerV2(images_post, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ImagesPostLogSerializerV2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 类视图
class CBVPostList(APIView):
    """
    列出所有的snippets或者创建一个新的snippet。
    """

    def get(self, request):
        snippets = ImagesPost.objects.all()
        serializer = ImagesPostLogSerializerV2(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ImagesPostLogSerializerV2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CBVPostDetail(APIView):
    """
    检索，更新或删除一个snippet示例。
    """

    def get_object(self, pk):
        try:
            return ImagesPost.objects.get(pk=pk)
        except ImagesPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        images_post = self.get_object(pk)
        serializer = ImagesPostLogSerializerV2(images_post)
        return Response(serializer.data)

    def put(self, request, pk):
        images_post = self.get_object(pk)
        serializer = ImagesPostLogSerializerV2(images_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        images_post = self.get_object(pk)
        images_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 使用混合（mixins）
class ImagesPostList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = ImagesPost.objects.all()
    print(queryset)
    serializer_class = ImagesPostLogSerializerV2
    print(serializer_class)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ImagesPostDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = ImagesPost.objects.all()
    serializer_class = ImagesPostLogSerializerV2

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookInfoGenericAPIView(GenericAPIView):
    queryset = ImagesPost.objects.all()  # 必须申明当前视图类中操作的模型数据是什么
    print(queryset)
    serializer_class = ImagesPostLogSerializerV2  # 可以声明当前要调用的序列化器是什么

    def get(self, request):
        print("reqeust的数据是", request)  # <rest_framework.request.Request object at 0x000000FA185102B0> 对象
        # 第一步：操作数据 获取所有数据
        data_list = self.get_queryset()
        print("data_Lists数据是", data_list)  # 从数据库中查询到的QuerySet 数据 列表
        # 第二步  序列化
        serializer = self.get_serializer(instance=data_list, many=True)
        print("serializer的数据是>>", serializer.data[0].get("modified_nation"))  # 获取到键值了

        # 第三步L：响应数据
        return Response(serializer.data)

# class PostViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin,
#                   mixins.RetrieveModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = ImagesPost.objects.all()
#     serializer_class = ImagesPostLogSerializerV2
#     print(queryset)
