# blog/views.py
"""
The blog app views.
"""
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from . import models

class HomeView(TemplateView):
    """
    The Home View Class Template View.
    """
    template_name = 'blog/home.html'

class AboutView(TemplateView):
    """
    The About View Class Template View.
    """
    template_name = 'blog/about.html'

class PostListView(ListView):
    """
    The Post List View.
    """
    model = models.Post
    context_object_name = 'posts'
    queryset = models.Post.objects.published().order_by('-published')

class PostDetailView(DetailView):
    """
    The Post Detail View.
    """
    model = models.Post

    def get_queryset(self):
        queryset = super().get_queryset().published()

        # If this is a `pk` lookup, use default queryset
        if 'pk' in self.kwargs:
            return queryset

        # Otherwise, filter on the published date
        return queryset.filter(
            published__year=self.kwargs['year'],
            published__month=self.kwargs['month'],
            published__day=self.kwargs['day'],
        )

class TopicListView(ListView):
    """
    The Topic List View.
    """
    model = models.Topic
    context_object_name = 'topics/'
    queryset = models.Topic.objects.all()

class TopicDetailView(DetailView):
    """
    The Topic Detail View.
    """
    model = models.Topic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topics_posts'] = models.Post.objects.filter(\
            topics__slug=self.kwargs['slug']).published().order_by('-published')

        return context

def terms_and_conditions(request):
    """
    The Terms and Conditions request function.
    """
    return render(request, 'blog/terms_and_conditions.html')

class ContactView(TemplateView):
    """
    The Contact View Class Template View.
    """
    template_name = 'blog/contact.html'
