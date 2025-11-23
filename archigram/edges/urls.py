from rest_framework.routers import DefaultRouter
from .views import EdgesViewSet, EdgeTypesViewSet

router = DefaultRouter()
router.register(r'edges', EdgesViewSet)
router.register(r'edges-type', EdgeTypesViewSet)
urlpatterns = router.urls