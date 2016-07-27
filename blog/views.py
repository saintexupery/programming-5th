from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'blog/post_list.html', {
        'post_list' : post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comment_list = Comment.objects.filter(post_id=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=pk)
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'comment_list' : comment_list,
        'form' : form,
    })