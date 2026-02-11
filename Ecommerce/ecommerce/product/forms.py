from django import forms
from product.models import Product 

"""
Two type of forms are there in django:
1. Form => we must define every custom field
2. ModelForm => django automatically define the forms on the basis of model
"""

"""Form"""
"""
There are two type of validation.
1. Field level validation => individual field laii valid garne e.g: email validation, password validation
2. Object level validation => two or more field ko bich maa validation lagaue e.g:
3. using Validators
"""
class LoginForm(forms.Form):
    email = forms.EmailField(label='User-Email', required=True)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(), label='User-Password')
    is_admin = forms.BooleanField()

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Password must be greater than 8 characters.")
        return password