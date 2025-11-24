from rest_framework.routers import DefaultRouter
from .views import POCViewSet

router = DefaultRouter()
router.register(r'data', POCViewSet, basename='data')
urlpatterns = router.urls