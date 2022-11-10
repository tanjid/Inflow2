from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # ...

    path('', MypageView.as_view(), name='reports_home'),
    path('product_report', ProductReport.as_view(), name='product_report'),

    # ...
]