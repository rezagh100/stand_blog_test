from django import forms


class ContactUsForm(forms.Form):
    text = forms.CharField(max_length=20, label='your massage')


