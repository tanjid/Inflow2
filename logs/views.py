from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from djangoproject.__init__ import KTLayout
from .models import OrderLog
from django.contrib import messages
from .forms import LogSearch
from orders.models import NewOrder
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


class LogsHomeView(TemplateView):
    template_name = 'logs/home.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # A function to init the global layout. It is defined in djangoproject/__init__.py file
        context = KTLayout.init(context)


        # context['log'] = OrderLog.objects.all()
        # KTTheme.addJavascriptFile('js/custom/test.js')
        
        context['form'] = LogSearch()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = LogSearch(request.POST)

        if form.is_valid():
            invoice_number = form.cleaned_data['invoive_number']
            try:
                order = NewOrder.objects.get(invoice_number=invoice_number)
                print(order)
                log = OrderLog.objects.filter(order = order)
                print(log)

                context['log'] = log
            except ObjectDoesNotExist:
                messages.add_message(request, messages.ERROR, f'No order with {invoice_number} ')
        return self.render_to_response(context)


class LogView(TemplateView):
    template_name = 'logs/log_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        invoice = self.kwargs['invoice']
        context["invoice"] = invoice
        try:
            order = NewOrder.objects.get(invoice_number=invoice)
            log = OrderLog.objects.filter(order = order)

            context['log'] = log
        except ObjectDoesNotExist:
                messages.add_message(self.request, messages.ERROR, f'No order with {invoice} ')
        context = KTLayout.init(context)

        return context