from django import forms


class registrationForm(forms.Form):
    Name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    Email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    phone_number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='Two Passwords Must be Same')

    def clean(self):
        cleaned_data = super(registrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class loginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
