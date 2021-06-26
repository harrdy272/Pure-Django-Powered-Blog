from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import BlogPost
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'

    def stores(self):
        return BlogPost.objects.values('label').distinct()

    def top_post(self):
        return BlogPost.objects.all()[:3]

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'

    def stores(self):
        return BlogPost.objects.values('label').distinct()
    
    def top_post(self):
        return BlogPost.objects.all()[:3]


