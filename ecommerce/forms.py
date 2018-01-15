from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class ContactForm(forms.Form):
    fullname= forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control","placeholder":"Name" ,"id":"form_full"}))
    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class":"form-control","placeholder":"Email" ,"id":"email"}))
    content=forms.CharField(
        widget=forms.Textarea(
            attrs={"class":"form-control","placeholder":"Type your content here","id":"form_content"}
        )
    )
    def clean_email(self):
        email =self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
class RegisterForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists")
        return username
    def clean_email(self):
        email=self.cleaned_data.get("email")
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email
    def clean(self):
        data=self.cleaned_data
        password=self.cleaned_data.get("password")
        password2=self.cleaned_data.get("password2")
        if password!=password2:
            raise forms.ValidationError("Passwords did not match")
        return data