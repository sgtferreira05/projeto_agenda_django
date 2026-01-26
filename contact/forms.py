from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'acept': 'image/*',
            }
        ),
        required=False,
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'category', 'description',
            'picture',
        )
 
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name and last_name:
            if first_name.lower() == last_name.lower():
                self.add_error(
                    'last_name',
                    ValidationError(
                        'Last name cannot be the same as first name.',
                        code='invalid',
                    )
                )

        # self.add_error(
        #     None,
        #     ValidationError(
        #         'Custom clean method error.',
        #         code='invalid',
        #     )
        # )
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == "django":
            self.add_error(
                'first_name',
                ValidationError(
                    'First name must not contain "django".',
                    code='invalid',
                )
            )
        return first_name

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)



    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Email is already in use.',
                    code='invalid',
                )
            )
        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        min_length=2,
        required=True,
        help_text='Required. 2-30 characters.',
        error_messages={
            'min_length': 'First name must be at least 2 characters long.',
        }
    )
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(), 
        required=False,
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='Enter the same password as before, for verification.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password1 = cleaned_data.get('password1')
        if password1:
            user.set_password(password1)
        if commit:
            user.save()
        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError(
                        'The two password fields didn’t match.',
                        code='invalid',
                    )
                )
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if email != current_email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Email is already in use.',
                        code='invalid',
                    )
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1, self.instance)
            except ValidationError as erros:
                self.add_error(
                    'password1',
                    ValidationError(
                        erros,
                        code='invalid',
                    )
                )
        return password1
