from django import forms
from .models import CustomUser, Product

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'customUseraddress']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['brand', 'price'] 

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class BasketAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int
    )
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class PaymentForm(forms.Form):
    card_number = forms.CharField(label='Card Number', max_length=16)
    expiration_date = forms.CharField(label='Expiration Date', max_length=5)
    cvv = forms.CharField(label='CVV', max_length=3)