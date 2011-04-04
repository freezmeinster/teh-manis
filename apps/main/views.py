from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from main.forms import UserRegistrationForm

def home(request):
    return render_to_response('main/index.html',{
    'url' : 'home',
    },context_instance=RequestContext(request))
    
def register(request,apps_id):
   
    if apps_id == 1 :
        redirect_url = 'kotakuang_home'
    else :
        redirect_url = 'main'
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
        
    return render_to_response('main/register.html',{
    'form': UserRegistrationForm(),
    'url' : 'register',
    },context_instance=RequestContext(request))
