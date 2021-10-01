from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import generic
from .models import Profile
from post.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

class UserDetail(generic.DetailView):
    template_name = 'user_detail.html'
    context_object_name = 'user_profile'
    model = User
    
    def get_slug_field(self):
        """Get the name of a slug field to be used to look up by slug."""
        return 'username'

    """
    def get_object(self):
       return Profile.objects.filter(user__username=self.kwargs.get('username'))

    """
    def get_context_data(self, **kwargs):
                context = super(UserDetail, self).get_context_data(**kwargs)
                context['post_list'] = Post.objects.filter(host__username__iexact=self.get_object().username)
                context['profile_object'] = Profile.objects.filter(user__username=self.get_object().username).first()
                print(context['profile_object'])
                #print(self.get_object().username)
                return context

@login_required(login_url='/login/')
def edit_user(request):
    template = 'edit_user.html'
    return render(request, template)

