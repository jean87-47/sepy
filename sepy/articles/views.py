from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .forms import ArticleForm,CommentForm
from .models import Article,Comment
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'articles/index.html')

@login_required
def create(request) :
    if request.method=='POST':
        form=ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.user=request.user
            article.save()
        return redirect('articles:index')

    else:
        form=ArticleForm()
        context={'form':form}

    return render(request,'articles/create.html',context)

def new(request):
    return render(request,'articles/new.html')

def new_create(request) :
   title=request.GET.get('title')
   content=request.GET.get('content')
   image=request.GET.get('image')
   article=Article(title=title,content=content,image=image)
   article.save()
   return redirect('articles:list')


def list(request) :

    articles=Article.objects.order_by('-created_date')
    context={'articles': articles}
    return render(request,'articles/list.html',context)

def detail(request,pk):
    article=get_object_or_404(Article,pk=pk)
    form=CommentForm()
    context={'article':article,
             'form' : form
             }
    return render(request,'articles/detail.html',context)


@login_required
def delete(request,pk):
    article=Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
        return redirect('articles:list')

    else:
        return HttpResponse('글쓴이만 지울 수 있어요')

@require_POST
def edit(request,pk) :
   article=get_object_or_404(Article,pk=pk)
   if request.user == article.user:
    if request.method=="POST":
        form=ArticleForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            article=form.save(commit=False)
            image=request.FILES.get('image')

            article.image=image
            article.save()
        return redirect('articles:list')
    else :
        form = ArticleForm(instance=article)
        context={'form':form}
    return render(request,'articles/create.html',context)

def edit_get(request,pk):
    article = Article.objects.get(pk=pk)
    context={'article': article}
    return render(request,'articles/update_get.html',context)


def update_get(request,pk):
    article=Article.objects.get(pk=pk)
    title=request.GET.get('title')
    content=request.GET.get('content')
    image=request.GET.get('image')
    article.title=title
    article.content=content
    article.image=image
    article.save()
    return redirect('articles:list')

@require_POST
def comments(request,pk) :
    article=get_object_or_404(Article,pk=pk)
    if request.user.is_authenticated:
         form=CommentForm(request.POST)
         if form.is_valid():
             comment=form.save(commit=False)
             comment.user=request.user
             comment.article=article
             comment.save()
         return redirect('articles:detail',pk=article.pk)
    else:
         return HttpResponse('댓글이나 질문을 남기시려면 로그인 하시기 바랍니다.' )

def comment_delete(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('articles:detail',pk=comment.article.pk)

def like(request,pk):
    article=get_object_or_404(Article,pk=pk)
    if request.user in article.like_users.all():
      article.like_users.remove(request.user)
    else:
      article.like_users.add(request.user)
    return redirect('articles:detail',pk=article.pk)




