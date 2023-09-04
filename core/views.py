from typing import Any

from django import forms
from django.contrib.auth import views as auth_views
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


class TestForm(forms.Form):
    char_field = forms.CharField(widget=forms.TextInput)
    text_area = forms.CharField(widget=forms.Textarea)
    number_input = forms.IntegerField(widget=forms.NumberInput)
    email_input = forms.EmailField(widget=forms.EmailInput, required=True)
    url_input = forms.URLField(widget=forms.URLInput, help_text="Help text here", required=True)
    password_input = forms.CharField(widget=forms.PasswordInput)
    date_input = forms.DateField(initial="2000-01-01")
    datetime_local_input = forms.DateTimeField()
    time_input = forms.TimeField(widget=forms.TimeInput)
    checkbox_input = forms.BooleanField(widget=forms.CheckboxInput, required=True, help_text="Hellooooo help")
    select = forms.ChoiceField(choices=[("1", "First"), ("2", "Second")], widget=forms.Select)
    null_boolean_select = forms.NullBooleanField(widget=forms.NullBooleanSelect)
    select_multiple = forms.MultipleChoiceField(choices=[("1", "First"), ("2", "Second")], widget=forms.SelectMultiple)
    radio_select = forms.ChoiceField(choices=[("1", "First"), ("2", "Second")], widget=forms.RadioSelect)
    checkbox_select_multiple = forms.MultipleChoiceField(
        choices=[("1", "First"), ("2", "Second")], widget=forms.CheckboxSelectMultiple, help_text="Hellooooo help"
    )
    file_input = forms.FileField(widget=forms.FileInput)
    clearable_file_input = forms.FileField(widget=forms.ClearableFileInput)
    split_datetime = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget)
    select_date = forms.DateField(widget=forms.SelectDateWidget)


def root(request: HttpRequest) -> HttpResponse:
    context = {"form": TestForm()}

    return render(request, "pages/root.html", context)


class LoginView(auth_views.LoginView):
    template_name = "pages/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    template_name = "pages/logout.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, self.get_context_data())
