from django import forms
from django.contrib.auth.models import User

# Login Form
class CandidateLoginForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['username', 'password']
        # widgets = {
        #     'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }