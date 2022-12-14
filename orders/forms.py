from django.forms import ModelForm
from django import forms
from .models import DeliveryMethod
from products.models import Product


class NewDeliveryMethodForm(ModelForm):
    class Meta:
        model = DeliveryMethod
        fields = '__all__'

        def __init__(self, *args, **kwrags):
            super(NewDeliveryMethodForm, self).__init__(*args, **kwrags)


            for k, v in self.fields.items():
                v.widget.attrs.update({'class': 'form-control'})

GEEKS_CHOICES =(
    (0, 0),
    (50, 50),
    (100, 100),
)
class NewOrderForm(forms.Form):
    
    name = forms.CharField()
    number = forms.CharField()
    # delivery_method = forms.ModelChoiceField(queryset=DeliveryMethod.objects.all())
    address = forms.CharField(widget=forms.Textarea())
    order_note = forms.CharField(widget=forms.Textarea(), required=False)
    # sku = forms.ModelChoiceField(queryset=Product.objects.all())
    # qty = forms.IntegerField()
    # price = forms.IntegerField()
    # item_total = forms.IntegerField(initial=0)
    sub_total = forms.IntegerField(initial=0)
    advance = forms.IntegerField(required=False)
    discount = forms.IntegerField(required=False)
    delivery_charge = forms.ChoiceField(choices = GEEKS_CHOICES)
    grand_total = forms.IntegerField()