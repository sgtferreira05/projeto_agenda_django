
from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'acept': 'image/*',
            }
        ),
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
