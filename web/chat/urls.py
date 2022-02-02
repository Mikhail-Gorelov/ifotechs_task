from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from main.views import TemplateAPIView

from . import views

app_name = 'chat'

router = DefaultRouter()
router.register(r'main', views.ChatViewSet, basename='main')

urlpatterns = [
    path('', TemplateAPIView.as_view(template_name='chat/index.html'), name='index'),
    path('last-messages/', views.LastMessagesView.as_view(), name="last-messages"),
    path('rest-websocket/', views.RestAndWebsocketView.as_view(), name="rest-websocket"),
    path('test-userchat/', views.TestUserChatView.as_view(), name="test-userchat"),
    path('chat-list/', views.UserChatView.as_view(), name="chat-list"),
    path('message-list/<chat_id>/', views.MessageChatView.as_view(), name="message-list"),
    path('message-last/<chat_id>/', views.LastChatMessage.as_view(), name="message-list"),
    path('init/', views.ChatInitView.as_view(), name="index"),
    path('short-info/', views.ChatShortInfoView.as_view(), name='short-info'),
    path('manage-items/', views.ManageRedisItems.as_view(), name="items"),
    path('manage-items/<slug:key>', views.ManageRedisItem.as_view(), name="single_item")
]

urlpatterns += router.urls
