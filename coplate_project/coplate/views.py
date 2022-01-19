from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from django.views.generic import ListView, DetailView, CreateView
from coplate.forms import ReviewForm
from coplate.models import Review

# Create your views here.
class IndexView(ListView):
    model = Review
    template_name = "coplate/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["-dt_created"]

class ReviewDetailView(DetailView):
    model = Review
    template_name = "coplate/review_detail.html"
    pk_url_kwarg = "review_id"

class ReviewCreateView(CreateView):
    model = Review
    template_name = "coplate/review_form.html"
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(self)
    
    def get_success_url(self):
        return reverse('review-detail', kwargs={"review_id":self.object.id})
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")