from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(help_text='Enter a valid email')
    password = forms.CharField()

    def clean_username(self):
        data = self.cleaned_data['username']
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        return data