from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def forum(request):
    return render(request, 'blog/forum.html', {})

def about(request):
    return render(request, 'blog/about.html', {})
