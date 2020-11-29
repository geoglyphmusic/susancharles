from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_view(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/blog.html', context)

def post_view(request, post_slug):
    context = {
        'post': get_object_or_404(Post, slug=post_slug)
    }
    return render(request, 'blog/post.html', context)

def tag_view(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'posts': posts,
    }
    return render(request, 'blog/tag.html', context)
