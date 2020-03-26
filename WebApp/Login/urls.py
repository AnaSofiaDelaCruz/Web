from Login.views import Index
from Login.views import Landing
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
	#URL QUE MANEJAN LOS PARAMETROS DASHBOARD
app_name = 'Login'
urlpatterns = [
    path('', views.Landing,name='Landing'),
    path('login/', views.Index,name='Login'),
]