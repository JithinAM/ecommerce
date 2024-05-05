from django import forms

class ProductSearchForm(forms.Form):
    search_term = forms.CharField(label='Search Product', max_length=100)
