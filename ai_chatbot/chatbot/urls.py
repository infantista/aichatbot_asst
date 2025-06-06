from django.urls import path
from .views import RegisterView, LoginView, ChatBotView, ChatHistoryView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('chat', ChatBotView.as_view(), name='chat'),
    path('chat/history', ChatHistoryView.as_view(), name='chat-history'),
]