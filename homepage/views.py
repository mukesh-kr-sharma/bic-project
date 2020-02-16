from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms

# Create your views here.
class Homepage(TemplateView):
    template_name = 'homepage/index.html'
    extra_context = {
        'candidate_login_form': forms.CandidateLoginForm,
    }
    def get_context_data(self, *args, **kwargs):
        context = super(Homepage, self).get_context_data(*args, **kwargs)
        context.update(self.extra_context)
        return context
