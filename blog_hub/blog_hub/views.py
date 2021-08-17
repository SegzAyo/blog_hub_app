from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog_hub/home.html', {'posts':posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('post_detail')
    else:
        form = CommentForm()

        context = {
            'post': post,
            'form': form,
        }
         
    return render(request, 'blog_hub/post_detail.html', context)  
