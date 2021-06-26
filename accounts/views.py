from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from posts.models import BlogPost

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    # def stores(self):
    #     return BlogPost.objects.values('label').distinct()

    # def top_post(self):
    #     return BlogPost.objects.all()[:3]