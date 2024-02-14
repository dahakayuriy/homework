from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import generic


class MyForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)
    list = forms.CharField(max_length=50)
    list2 = forms.CharField(max_length=50)
    list3 = forms.CharField(max_length=50)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def return_simple_html(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Виконайте потрібні дії з валідною формою
            pass
    else:
        form = MyForm()

    blog_entries = [
        {
            "title": "Cthulhu",
            "body": "Death May Die (Cthulhu: Death May Die)",
            "list": "Horror",
            "list2": "Mysticism",
            "list3": "Occultism",
        }
    ]

    return render(request, 'child.html', {'form': form, 'blog_entries': blog_entries})
