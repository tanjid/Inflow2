from django import forms
from .models import Product, ProductBrand

class AdjustStockForm(forms.Form):
    sku = forms.ModelChoiceField(queryset=Product.objects.all())
    qty = forms.IntegerField(initial=0)
    CAUSE_CHOICES = (
    ("Damaged", "Damaged"),
    ("Lost", "Lost"),
    ("Unknown", "Unknown"),

)
    cause =forms.ChoiceField(choices = CAUSE_CHOICES, initial='Damaged', widget=forms.Select(), required=True)
    note = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class NewBrandForm(forms.ModelForm):
    class Meta:
        model = ProductBrand
        fields = "__all__"