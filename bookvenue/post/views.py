from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.

class PostListView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(generic.DetailView):
    template_name  = 'detail.html'
    model = Post
    slug_url_kwarg = 'slug'

@login_required
def create_post(request):
    template = 'create-post.html'
    form = PostForm(data = request.POST or None)
    context = {'form': form}
    if(request.method == 'POST'):
            form.instance.host = request.user
            form.instance.date_posted = datetime.now()
            form.save()
            return redirect('/post/')
    return render(request, template, context)
        


