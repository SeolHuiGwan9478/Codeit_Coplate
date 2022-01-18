from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import ListView
from coplate.models import Review

# Create your views here.
class IndexView(ListView):
    model = Review
    template_name = "coplate/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["-dt_created"]

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")