from django.shortcuts import render, get_object_or_404
from blog.models import Post
from .forms import  CommentForm
from .models import Post,Comment
from django.contrib.auth.decorators import login_required

def index(request):
# get the blog posts that are published
	posts = Post.objects.filter(published=True)
# now return the rendered template
	return render(request, 'blog/index.html', {'posts': posts})

def post(request, slug):
# get the Post object
	post = get_object_or_404(Post, slug=slug)
# now return the rendered template
	return render(request, 'blog/post.html', {'post': post})
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
