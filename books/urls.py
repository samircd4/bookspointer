from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AppUserViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'users', AppUserViewSet, basename='user')

urlpatterns = router.urls
