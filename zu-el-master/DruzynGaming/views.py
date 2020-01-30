from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, Player
from django.views.generic import ListView, DetailView,View
from django.http import HttpResponseRedirect,HttpResponse

#home view for posts. Posts are displayed in a list


class IndexView(ListView):
 template_name='DruzynGaming/aktualnosci.html'
 context_object_name = 'post_list'
 def get_queryset(self):
  return Post.objects.all()
#Detail view (view post detail)
class PostDetailView(DetailView):
 model=Post
 template_name = 'DruzynGaming/post-detail.html'
#New post view (Create new post)
def postview(request):
 if request.method == 'POST':
  form = PostForm(request.POST)
  if form.is_valid():
   form.save()
  return redirect('aktualnosci')
 form = PostForm()
 return render(request,'DruzynGaming/post.html',{'form': form})
#Edit a post
def edit(request, pk, template_name='DruzynGaming/edit.html'):
    post= get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('aktualnosci')
    return render(request, template_name, {'form':form})
#Delete post
def delete(request, pk, template_name='DruzynGaming/confirm_delete.html'):
    post= get_object_or_404(Post, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('aktualnosci')
    return render(request, template_name, {'object':post})

def aktualnosci(request,template_name='DruzynGaming/aktualnosci.html'):
    post=get_object_or_404(Post)
    if request.method=='POST':
        post.aktualnosci()
        return redirect('aktualnosci')
    return render(request,template_name,{'object':post})

def harmonogram(request,template_name='DruzynGaming/harmonogram.html'):
    
    if request.method=='POST':
        post.aktualnosci()
        return redirect('harmonogram')
    return render(request,template_name)

def sekcje(request,template_name='DruzynGaming/sekcje.html'):
    if request.method=='POST':
        post.aktualnosci()
        return redirect('sekcje')
        return Post.objects.all()
