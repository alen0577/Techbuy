from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Shop
from .forms import ModelForm


# Create your views here.
def home(request):
    product = Shop.objects.all()
    return render(request, 'home.html', {'products': product})


def detail(request, shop_id):
    product1 = Shop.objects.get(id=shop_id)
    return render(request, 'detail.html', {'product': product1})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        des = request.POST.get('des')
        img = request.FILES['img']
        price = request.POST.get('price')
        s = Shop(name=name, des=des, img=img, price=price)
        s.save()
        print('product added')
        return redirect('/')

    return render(request, 'add_product.html')


def update(request, id):
    obj = Shop.objects.get(id=id)
    form = ModelForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'obj': obj})


def delete(request,id):
    if request.method == "POST":
        obj = Shop.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request, 'delete.html')
