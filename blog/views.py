
from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Raunak Sharma',
        'title':'First Post',
        'content':'Look I have cretaed a post.soorty two errors.',
        'date_posted':'August 27,2018'
    },
     {
        'author':'Raunak Sharma',
        'title':'second Post',
        'content':'Look I have cretaed another post.soorty two errors.',
        'date_posted':'August 27,2018'
    },
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})


