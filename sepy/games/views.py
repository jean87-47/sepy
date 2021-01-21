from django.shortcuts import render,redirect
import random
from .forms import KeyForm

def index(request):
    return render(request,'games/index.html')

# Create your views here.
def lotto(request) :
    import random
    pick=random.sample(range(1,46),6)
    context={'pick':pick}
    return render(request,'games/lotto.html',context)

def pick_present(request):
    presents=['perfume','ring','diamond','car','cat','cosmetics']
    present=random.choice(presents)
    context={'presents':presents,
              'present':present}
    return render(request,'games/pick_present.html',context)

def hi(request,name):
    context={'name':name}
    return render(request,'games/hi.html',context)

def add(request,a,b):
    result=a+b
    context={'result':result,
             'a':a,
             'b':b,
             }
    return render(request,'games/add.html',context)

def number(request):
    pick=random.sample(range(1,46),2)
    c=pick[0]
    d=pick[1]
    context={'c':c,
             'd':d
             }
    return render(request,'games/index.html',context)

def posts(request,id):
    user='sepy'
    replies=['good','bad','worthy','useful']
    content='Life is good'
    no_replies=[]
    context={
        'user':user,
        'replies': replies,
        'no_replies': no_replies,
        'id':id,
        'content':content
    }
    return render(request,'games/posts.html',context)


def key(request):
    return render(request,'games/key.html')

def key(request) :
    if request.method=='POST':
        form=KeyForm(request.POST,request.FILES)
        if form.is_valid():
            key=form.save(commit=False)
            key.save()
            number=request.POST.get('key')
            if number=='tmj2021':
                return redirect('games:index')

    else:
        form=KeyForm()
        context={'form':form}

    return render(request,'games/key.html',context)
