from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Internal Routes
router.register(r'parents', views.ParentViewSet)
router.register(r'parents/child', views.ChildViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
