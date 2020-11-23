from django.shortcuts import render, get_object_or_404
from .models import Post

def blog(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/blog.html', context)

def post(request, post_slug):
    context = {
        'post': get_object_or_404(Post, slug=post_slug)
    }
    return render(request, 'blog/post.html', context)
