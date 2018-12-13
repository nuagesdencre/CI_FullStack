from django import forms
from .models import Order


class MakePaymentForm(forms.Form):
    """
    Gather the necessary information to process a card payment with Stripe
    """
    MONTH_CHOICES = [(i, i) for i in range(1, 12 + 1)]
    YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """
    Display required information from the user before his/her payment can be processed
    """
    class Meta:
        model = Order
        fields = (
            'full_name', 'phone_number', 'address_line_1', 'address_line_2', 'town_or_city', 'postcode',
            'county', 'country')
