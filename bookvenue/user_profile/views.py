from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import generic
from .models import Profile
from post.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


# Create your views here.

class UserDetail(generic.DetailView):
    template_name = 'user_detail.html'
    context_object_name = 'user_profile'
    model = User
    form = ProfileForm
    
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
                user = self.request.user
                if(user.is_authenticated):
                    if(self.get_object() == user):
                        context['my_profile'] = True
                    else:
                        context['my_profile'] = False
                    context['name'] = user.username
                    context['authenticated'] = True
                else:
                    context['my_profile'] = False
                    context['name'] = 'anonymous'
                    context['authenticated'] = False
                #print(context)
                return context

class ProfileUpdateView(generic.UpdateView):
    model = Profile
    fields = ('bio', 'city', 'country', 'phonenumber', 'birth_date', 'profile_picture')
    template_name = 'edit_user.html'

    def get_object(self):
        user = self.request.user
        if not user.is_authenticated:
            return redirect('/login/')
        return Profile.objects.get(user=user)

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['profile_object'] = self.get_object()
        context['my_profile'] = True
        context['authenticated'] = True
        context['name'] = self.request.user.username
        return context

    def get_success_url(self, **kwargs):
        username = self.request.user.username
        return '/user/' + username + '/'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.save()
    #     return super().form_valid(form)

