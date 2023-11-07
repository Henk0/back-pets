from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
  ListAPIView, CreateAPIView,
  RetrieveUpdateAPIView,
  RetrieveAPIView,
  DestroyAPIView
)
from rest_framework import pagination
from rest_framework.permissions import (
 IsAuthenticatedOrReadOnly
)
from ...core.pagination import PostLimitOffsetPagination
from .serializers import TABLE, RequestsSerializer, RequestsCreateSerializer


class RequestsListAPIView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RequestsSerializer
    pagination_class = PostLimitOffsetPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = TABLE.objects.all()

        page_size_key = 'page_size'
        page_size = self.request.GET.get(page_size_key)
        query = self.request.GET.get('q')
        author = self.request.GET.get('uid')
        pagination.PageNumberPagination.page_size = page_size if page_size else 10
        
        if author:
            queryset_list = queryset_list.filter(
                author=author
            )

        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        return queryset_list.order_by('updated_at')


class RequestsCreateAPIView(CreateAPIView):
    serializer_class = RequestsCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        print(request.data)
        serializer = RequestsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestsDetailAPIView(RetrieveAPIView):
    queryset = TABLE.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RequestsSerializer


class RequestsDeleteAPIView(DestroyAPIView):
    queryset = TABLE.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = RequestsSerializer


class RequestsUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = TABLE.objects.all()
    serializer_class = RequestsSerializer
