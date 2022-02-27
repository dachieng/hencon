from django import forms

class EmailUs(forms.Form):
    email = forms.EmailField(label="Email :", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Email'}))
    

   
    

