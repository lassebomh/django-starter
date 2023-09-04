from django import forms
from django_unicorn.components import UnicornView


class BookForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    publish_date = forms.DateTimeField(required=True)


class FormcomponentView(UnicornView):
    form_class = BookForm

    title = ""
    publish_date = ""
