from django.http import Http404
from django.contrib import  messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from .models import Post, Comment
from .forms import CommentModelForm, CommentForm

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
        form = CommentModelForm(request.POST, request.FILES)
        form2 = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=pk)
            comment.save()
            # print(request.POST) : 커맨드에 프린트가 됨.
            messages.success(request, '새 댓글을 저장했습니다.')
            return redirect('blog:post_detail', pk)
        if form2.is_valid():
            formInstance = CommentFrom(post=request.post)
            formInstance.author = form2.cleaned_data['author']
            formInstance.message = form2.cleaned_data['message']
            formInstance.jjal = form2.cleaned_data['jjal']
            return redirect('/')

    else:
        form = CommentModelForm()
        form2 = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post' : post,
        'form' : form,
        'form2' : form2,
    })


def comment_edit(request, post_pk, comment_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = Comment.objects.get(post_id=post_pk, pk=comment_pk)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save()
            messages.success(request, '댓글을 수정하였습니다.')
            return redirect(post)
#            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentModelForm(instance=comment)

    return render(request, 'blog/comment_edit.html', {
        'form' : form,
    })
