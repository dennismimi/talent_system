from django import forms
import logging
from django.contrib.auth import authenticate
from django.contrib.auth.forms import (UsernameField, UserCreationForm as DjangoUserCreationForm)
from .models import Student, User, Receipt, Fees_paid

logger = logging.getLogger(__name__)


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = User
        fields = ("email",)
        field_classes = {"email": UsernameField}

    def send_mail(self):
        logger.info(
            "Sending signup email for email=%s",
            self.cleaned_data["email"],
        )
        message = "Welcome{}".format(self.cleaned_data["email"])


class AuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        strip=False, widget=forms.PasswordInput
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        if email is not None and password:
            self.user = authenticate(
                self.request, email=email, password=password
            )
            if self.user is None:
                raise forms.ValidationError(
                    "Invalid email/password combination."
                )
            logger.info(
                "Authentication successful for email=%s", email
            )
        return self.cleaned_data

    def get_user(self):
        return self.user


class Medical_Search(forms.Form):
    text_search = forms.CharField(widget=forms.TextInput)

    def clean_field(self):
        if text_search == '' or text_search is None:
            raise forms.ValidationError(
                "Invalid search.It should not be empty"
            )
        text_search = self.cleaned_data["text_search"]

        return data
