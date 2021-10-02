from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime

# Create your views here.

class PostDetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Post
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        c = super(PostDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        #print(self.get_object().host.username)
        if(user.is_authenticated):
            c['name'] = user.username
            c['profile_picture'] = user.profile.profile_picture
            c['authenticated'] = True
            if(user != self.get_object().host):
                self.get_object().is_clicked()
        else:
            c['name'] = 'anonymous'
            c['authenticated'] = False
            self.get_object().is_clicked()
        print(c['name'])
        return c

@login_required(login_url='/login/')
def create_post(request):
    template = 'create-post.html'
    form = PostForm()
    context = {'form': form}
    if(request.method == 'POST'):
            form = PostForm(request.POST, request.FILES)
            form.instance.host = request.user
            form.instance.date_posted = datetime.now()
            form.save()
            return redirect('/')
    return render(request, template, context)
        


