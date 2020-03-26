from django.shortcuts import render
from django.views.generic import View
 # Create your views here.
# def Index (request):
#     return render(request,'Login.html',{})

# def Landing (request):
#     return render(request,'Vista.html',{})

class LoginClass(views):
    # template = 'Login'
    # def get(self, request, *args, **kwargs):
    #     return render(request,)
    templates = 'Login/login.html'
    template_ok = 'Dashboard/dashboard.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.templates,{})
    
    def post(self,request,*args,**kwargs):
        user_post = request.POST['user']
        password_post = request.POST['password']

        user_session = authenticate(username = user_post,password = password_post)

        if user_session is not None:
            return render(request, self.template_ok,{})
        else:
            self.message = 'Usuario o contraseña incorrecta'
        return render(request,self.templates, self.get_context())
    
    def get_context(self):
        return {
            'Error':self.message,
        }