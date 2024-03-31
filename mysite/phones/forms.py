from django import forms
form .models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['name', 'price', 'description']