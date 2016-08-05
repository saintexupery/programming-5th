from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def post_list(request):
    post_list = Post.objects.all()

    return render(request, 'blog/post_list.html', {
        'post_list' : post_list,
    })

def post_detail(request, pk):
    # try:
    #     post = Post.objects.get(pk=pk) # Post.DoesNotExist 에러가 게시물 삭제시 발생할 수 있다.
    #     comment_list = Comment.objects.filter(post_id=pk)
    # except:
    #     raise Http404
    # 위와 같이 적는 것은 번거로울 수 있다. 이런 상황에서 제공되는 기능이 get_object_or_404 Function.

    post = get_object_or_404(Post, pk=pk)

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
        'form' : form,
    })


def comment_edit(request, post_pk, comment_pk):
    comment = Comment.objects.get(post_id=post_pk, pk=comment_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/comment_edit.html', {
        'form' : form
    })
