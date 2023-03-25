from django.shortcuts import render, redirect

from blogProject.models import Post

from .forms import CommentForm

# Create your views here.

def frontpage(request):

    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {"posts": posts})

def detailPage(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
    	form = CommentForm(request.POST)

    	if form.is_valid():
    		comment = form.save(commit=False)
    		comment.post = post
    		comment.save()

    		return redirect('detail', slug=post.slug)
    else:
    	form = CommentForm()

    return render(request, 'blog/postdetail.html', {'post': post, 'form': form})