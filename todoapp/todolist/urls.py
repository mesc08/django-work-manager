from rest_framework import routers
from .api import todolistViewSet

router = routers.DefaultRouter()
router.register('todolists', todolistViewSet, 'todolists')

urlpatterns = router.urls