from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from blog.forms import BlogForm
from blog.models import Blog
from catalog.views import AccessСheckMixinView


class BlogCreateView(AccessСheckMixinView, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)[:20]
            new_article.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(AccessСheckMixinView, UpdateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)[:20]
            new_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:view", kwargs={"slug": self.object.slug})


class BlogDeleteView(AccessСheckMixinView, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
