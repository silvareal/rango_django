from blaze.models import Category
from django.shortcuts import  render, get_object_or_404


def index(request):
    category_list = Category.objects.order_by('-like')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'blaze/index.html', context_dict)

def about(request):
    context_dict={ }
    return render(request, 'blaze/about.html', context_dict)