from django import forms


class SendEmail(forms.Form):
    name = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    massage = forms.Textarea(widget=forms.Textarea)
    
    def send_email(self):
        pass