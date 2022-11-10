from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from djangoproject.__init__ import KTLayout
from djangoproject.libs.theme import KTTheme
from orders.models import NewOrder, OrderDetails
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import get_current_timezone
import pytz
from django.db.models import Count
# Create your views here.

class MypageView(TemplateView):
    template_name = 'reports/reports_home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # A function to init the global layout. It is defined in djangoproject/__init__.py file
        context = KTLayout.init(context)

        # KTTheme.addJavascriptFile('js/custom/test.js')
        
        return context


class ProductReport(TemplateView):
    template_name = 'reports/product_report.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        last_month = (datetime.now(tz=get_current_timezone()).today()-timedelta(days=30)).date()
        last_week = (datetime.now(tz=get_current_timezone()).today()-timedelta(days=7)).date()
        today = datetime.now(tz=get_current_timezone()).today().date()
        print(f"today: {today}")
        context = super().get_context_data(**kwargs)
        context = KTLayout.init(context)

        last_month_orders = OrderDetails.objects.filter(main_order__created_at__date__gt = last_month)
        last_week_orders = last_month_orders.filter(main_order__created_at__date__gt = last_week)
        todays_orders = last_week_orders.filter(main_order__created_at__date = today)
        sku_count = {}

        for i in todays_orders:
            if i.sku in sku_count:
                sku_count[i.sku] = sku_count.get(i.sku) + i.qty
            else:
                sku_count[i.sku] = i.qty

        sku_count = sorted(sku_count.items(), key=lambda x: x[1], reverse=True) 
        sku_count = dict(sku_count)
        limit = 10
        first_n = dict(zip(list(sku_count.keys())[:limit], list(sku_count.values())[:limit]))
        context['todays_orders'] = first_n



        sku_count1 = {}

        for i in last_week_orders:
            if i.sku in sku_count1:
                sku_count1[i.sku] = sku_count1.get(i.sku) + i.qty
            else:
                sku_count1[i.sku] = i.qty

        sku_count1 = sorted(sku_count1.items(), key=lambda x: x[1], reverse=True) 
        sku_count1 = dict(sku_count1)
        limit = 10
        last_week_orders = dict(zip(list(sku_count1.keys())[:limit], list(sku_count1.values())[:limit]))
        context['last_week_orders'] = last_week_orders



        
        sku_count2 = {}

        for i in last_month_orders:
            if i.sku in sku_count2:
                sku_count2[i.sku] = sku_count2.get(i.sku) + i.qty
            else:
                sku_count2[i.sku] = i.qty

        sku_count2 = sorted(sku_count2.items(), key=lambda x: x[1], reverse=True) 
        sku_count2 = dict(sku_count2)
        limit = 10
        last_month_orders = dict(zip(list(sku_count2.keys())[:limit], list(sku_count2.values())[:limit]))
        print(f"last_month_orders {last_month_orders}")
        context['last_month_orders'] = last_month_orders

        # A function to init the global layout. It is defined in djangoproject/__init__.py file

        # KTTheme.addJavascriptFile('js/custom/test.js')
        
        return context