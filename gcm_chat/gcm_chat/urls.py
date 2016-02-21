from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from app.core.views import UserViewSet
from app.room.views import ChatRoomViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, base_name='user')
router.register(r'rooms', ChatRoomViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls), name='api')
]
