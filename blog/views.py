
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from blog.models import Post



# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request,'blog/home.html',context)


class postListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class postDetailView(DetailView):
    model = Post
   

def about(request):
    return render(request,'blog/about.html',{'title':'about'})


