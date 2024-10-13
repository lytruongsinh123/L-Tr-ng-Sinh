from django.shortcuts import render, get_object_or_404
from blogs.models import Post, Comment
from blogs.forms import CommentForm
from django.http import HttpResponseRedirect


def post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST,author=request.user, post = post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)

    return render(request, "blogs/post.html", {"post":post, "form":form})
