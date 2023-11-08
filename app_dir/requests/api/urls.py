from django.urls import path
from .views import (
    RequestsCreateAPIView,
    RequestsListAPIView,
    RequestsDeleteAPIView,
    RequestsDetailAPIView,
    RequestsUpdateAPIView,
    CommentListCreateAPIView,
    CommentDetailAPIView,
    RequestCommentsListAPIView
)

urlpatterns = [
    path('', RequestsListAPIView.as_view(), name='list'),
    path('create', RequestsCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', RequestsDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', RequestsDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', RequestsUpdateAPIView.as_view(), name='update'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:request_id>/', RequestCommentsListAPIView.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]
