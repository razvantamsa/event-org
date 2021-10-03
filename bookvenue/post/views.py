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

    def get_object(self, queryset=None, ok=True):
        item = super().get_object(queryset)
        print(item.clicked)
        user = self.request.user
        if( (user != item.host) and ok==True):
            item.is_clicked()
        #print(item.clicked)
        return item

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        c = super(PostDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        if(user.is_authenticated):
            c['name'] = user.username
            c['profile_picture'] = user.profile.profile_picture
            c['authenticated'] = True
            if(user == self.get_object(ok=False).host):
                c['my_post'] = True
            else:
                c['my_post'] = False

        else:
            c['name'] = 'anonymous'
            c['authenticated'] = False
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

@login_required(login_url='/login/')
def delete_post(request, slug):
    user = request.user
    post = Post.objects.get(slug=slug)
    if(post.host == user):
        title = post.title
        post.delete()
        context['message'] = 'Post named ' + title + ' was deleted.' 
    else:
        context['message'] = 'You do not have permission to delete.'
    redirect_url = '/user/' + user.username + '/'
    return redirect(redirect_url, context)

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = ('title', 'description', 'address','city', 'country', 'picture1', 'picture2', 'picture3', 'picture4')
    form = PostForm
    template_name = 'update.html'

    def get_queryset(self):
        queryset = super(PostUpdateView, self).get_queryset()
        return queryset.filter(host=self.request.user)


    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['profile_object'] = self.get_object()
        context['my_profile'] = True
        context['authenticated'] = True
        context['name'] = self.request.user.username
        return context

    def get_success_url(self, **kwargs):
        username = self.request.user.username
        return '/user/' + username + '/'
        


