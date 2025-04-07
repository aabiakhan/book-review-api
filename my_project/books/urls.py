from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewListCreateAPIView

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:book_id>/reviews/', ReviewListCreateAPIView.as_view(), name='book-reviews'),
]
