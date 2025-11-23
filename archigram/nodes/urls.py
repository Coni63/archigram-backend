from rest_framework.routers import DefaultRouter
from .views import NodesViewSet, NodeTypesViewSet

router = DefaultRouter()
router.register(r'nodes', NodesViewSet)
router.register(r'nodes-type', NodeTypesViewSet)
urlpatterns = router.urls