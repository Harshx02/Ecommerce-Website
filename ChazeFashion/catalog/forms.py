from django import forms
from .models import UserProfile

# --------- User Profile Form ---------
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'avatar']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'address': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full', 'rows': 3}),
            'avatar': forms.FileInput(attrs={'class': 'file-input file-input-bordered w-full'}),
        }

# --------- Cart Add Product Form ---------
class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'input input-bordered w-20'})
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput()
    )
