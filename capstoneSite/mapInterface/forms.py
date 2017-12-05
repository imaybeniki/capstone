from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def clean_username(self):
        data = self.cleaned_data['username']
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        return data