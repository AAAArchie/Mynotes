import json
from rest_framework import mixins, viewsets, status, generics
from django.http import HttpResponse, Http404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, action
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from post_app.models import TestPost
from post_app.serializer import TestPostLogSerializer


# CBV 类视图  DRF框架的视图的基类是 APIView
class CBVAPIViewList(APIView):
    """
    列出所有的TestPost或者创建一个新的TestPost。
    """

    def get(self, request):
        test_post = TestPost.objects.all()
        serializer = TestPostLogSerializer(test_post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestPostLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CBVAPIViewDetail(APIView):
    """
    检索，更新或删除一个TestPost示例。
    """

    def get_object(self, pk):
        try:
            return TestPost.objects.get(pk=pk)
        except TestPost.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        test_post = self.get_object(pk)
        serializer = TestPostLogSerializer(test_post)
        return Response(serializer.data)

    def put(self, request, pk):
        test_post = self.get_object(pk)
        serializer = TestPostLogSerializer(test_post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        test_post = self.get_object(pk)
        test_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 使用混合（mixins）
class TestPostMixinList(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView):
    queryset = TestPost.objects.all()
    print(queryset)
    serializer_class = TestPostLogSerializer
    print(serializer_class)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TestPostMixinDetail(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          generics.GenericAPIView):
    queryset = TestPost.objects.all()
    serializer_class = TestPostLogSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# 使用通用的基于类的视图
# 通过使用mixin类，我们使用更少的代码重写了这些视图，但我们还可以再进一步。
# REST框架提供了一组已经混合好（mixed-in）的通用视图，我们可以使用它来简化我们的views.py模块
class TestPostGenericAPIView(generics.GenericAPIView):
    queryset = TestPost.objects.all()  # 必须申明当前视图类中操作的模型数据是什么
    print(queryset)
    serializer_class = TestPostLogSerializer  # 可以声明当前要调用的序列化器是什么

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


class ListCreateAPIView(generics.ListCreateAPIView):
    queryset = TestPost.objects.all()
    serializer_class = TestPostLogSerializer


class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestPost.objects.all()
    serializer_class = TestPostLogSerializer


# 视图集
class TestPostViewSet(ViewSet):
    """
    没有这个属性要加上  # router.register(r'TestPostViewSet', views.TestPostViewSet, basename="post_post")
    queryset = TestPost.objects.all()
    serializer = TestPostLogSerializer(queryset, many=True)
    """

    """    
    getlist() 提供一组数据
    retrieve() 提供单个数据
    create() 创建数据
    update() 保存数据
    destory() 删除数据

    使用ViewSet通常并不方便，因为list、retrieve、create、update、destory等方法都需要自己编写，
    而这些方法与前面讲过的Mixin扩展类提供的方法同名，所以我们可以通过继承Mixin扩展类来复用这些方法而无需自己编写。
    但是Mixin扩展类依赖与GenericAPIView，所以还需要继承GenericAPIView。

    """

    def list(self, request):
        queryset = TestPost.objects.all()
        serializer = TestPostLogSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TestPost.objects.all()
        serializer = TestPostLogSerializer(queryset)
        return Response(serializer.data)


class TestPostViewSetV1(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    自定义视图类 GenericViewSet
    GenericViewSet帮助我们完成了继承工作，继承自GenericAPIView与ViewSetMixin，
    在实现了调用as_view()时传入字典（如{‘get’:‘list’}）的映射处理工作的同时，
    还提供了GenericAPIView提供的基础方法，可以直接搭配Mixin扩展类使用。
    """

    queryset = TestPost.objects.all()
    serializer_class = TestPostLogSerializer

    def get_queryset(self):
        return TestPost.objects.all()


class ReadOnly:
    pass


class TestPostViewSetV2(viewsets.ModelViewSet):
    """
    ModelViewSet继承自GenericViewSet，
    同时包括了ListModelMixin、RetrieveModelMixin、
    CreateModelMixin、UpdateModelMixin、DestoryModelMixin。
    """
    queryset = TestPost.objects.all()
    serializer_class = TestPostLogSerializer

    authentication_classes = [SessionAuthentication, BasicAuthentication]  # 局部认证

    permission_classes = [IsAuthenticated | ReadOnly]  # 局部权限

    throttle_scope = 'downloads'  # 局部自定义限流

    def get_queryset(self):
        return TestPost.objects.all()

    """
    action装饰器默认路由请求GET，但也可以通过设置methods参数接受其他 HTTP 方法。例如：
    @action(detail=True, methods=['post_app', 'delete'])
    """

    # http://127.0.0.1:8000/api/TestPostViewSetV2/action_test/

    @action(detail=False, methods=['get'], url_path="action_test")
    def action_test(self, request, *args, **kwargs):
        return Response("successful")
