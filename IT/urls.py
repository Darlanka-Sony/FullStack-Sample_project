"""
URL configuration for SRKR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from IT import views
from IT.views import StudentReg, Studentlist, Studentdetail, StudentUpdate, StudentDelete
app_name="IT"
urlpatterns = [
   path("home",views.home, name="home"),
   path('service',views.service, name="service"),
   path('contact',views.contact, name="contact"),
   path('products',views.products, name="products"),
   path('aboutus',views.aboutus, name="aboutus"),
   path('studentreg',StudentReg.as_view(),name='studentreg'),
   path('<pk>/studentdetail',Studentdetail.as_view(),name='studentdetail'),
   path('',Studentlist.as_view(),name='studentlist'),
   path('<pk>/studentupdate',StudentUpdate.as_view(),name='studentupdate'),
   path('<pk>/studentdelete',StudentDelete.as_view(),name='studentdelete'),
   path('student',views.student, name = 'student'),
   path('form', views.form,name  = 'form'),
   path('detail/<int:id>', views.detail, name = 'detail'),
   path('update/<int:id>', views.update, name = 'update'),
   path('delete/<int:id>', views.delete, name = 'delete'),
   path('rit',views.rit, name = 'rit'),
   path('get1', views.get1, name = 'get1'),
   path('post1', views.post1, name = 'post1'),
   path('index', views.index, name = 'index'),
   path('about', views.about, name = 'about'),
   path('blog', views.blog, name = 'blog'),
   path('contact', views.contact, name = 'contact'),
   path('portfolio', views.portfolio, name = 'portfolio'),
   path('blog_single', views.blog_single, name = 'blog_single'),
   path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),
]

