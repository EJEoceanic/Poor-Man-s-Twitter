from django.urls import path
from rest_framework import routers

from .views import TweetViewSet

router = routers.DefaultRouter()
router.register("", TweetViewSet)

urlpatterns = router.urls