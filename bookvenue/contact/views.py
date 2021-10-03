from django.shortcuts import render
from django.views import generic
from .models import Contact

# Create your views here.

class CreateContactView(generic.CreateView):
    model = Contact
    fields = '__all__'
    template_name = "contact.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        c = super(CreateContactView, self).get_context_data(**kwargs)
        user = self.request.user
        if(user.is_authenticated):
            c['name'] = user.username
            c['authenticated'] = True
            c['user_mail'] = user.email
        else:
            c['name'] = 'anonymous'
            c['authenticated'] = False
            c['user_mail'] = ''
        return c
