from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm

# Adding pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'posts': posts, 'page': page})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
        )
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html',
                  {
                      'post': post,
                      'comments': comments,
                      'comment_form': comment_form
                  })

