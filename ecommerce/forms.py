from django import forms

class ContactForm(forms.Form):
    fullname= forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control","placeholder":"Name" ,"id":"form_full"}))
    email=forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class":"form-control","placeholder":"Email" ,"id":"form_full"}))
    content=forms.CharField(
        widget=forms.Textarea(
            attrs={"class":"form-control","placeholder":"Type your content here","id":"form_content"}
        )
    )
    def clean_email(self):
        email =self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")