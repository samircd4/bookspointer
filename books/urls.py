from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AppUserViewSet, CategoryViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'users', AppUserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'authors', AuthorViewSet, basename='author')

urlpatterns = router.urls

