from django.urls import path
from .views import LogsHomeView, LogView

urlpatterns = [
    path('home/', LogsHomeView.as_view(), name='logs_home'),
    path('<str:invoice>/', LogView.as_view(), name='logs_view'),

]