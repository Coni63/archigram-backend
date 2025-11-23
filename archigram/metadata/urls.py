from rest_framework.routers import DefaultRouter
from .views import MetadataViewSet, MetadataConfigViewSet

router = DefaultRouter()
router.register(r'metadatas', MetadataViewSet)
router.register(r'metadatas-config', MetadataConfigViewSet)
urlpatterns = router.urls