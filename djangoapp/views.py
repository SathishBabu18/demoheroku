from django.shortcuts import render,redirect
from .models import product
# Create your views here.
from .forms import productForm


def home(request):
    result=product.objects.all()
    context={'output' : result}
    return render(request,'home.html',context)

def Product(request):
    return render(request,'product.html')

def service(request):
    return render(request,'service.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contact(request):
    return render(request,'contact.html')

def get_product(request): #create view
    if request.method =="POST":
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = productForm()
    return render(request, "form.html", {'form': form})

def detail_product(request, pk): # detail view
    Products = product.objects.get(pk = pk)
    context = {"product" :Products}
    return render(request, "detail.html", context)


def update_product(request,pk):
    products = product.objects.get(pk = pk)
    form = productForm(request.POST or None, instance =products)
    if form.is_valid():
        form.save()
        return redirect('home')
    
    context = {'product':product, "form":form}
    return render(request, "update.html", context)


def delete_product(request, pk): # detail view
    products = product.objects.get(pk = pk)
    context = {"product" :products}
    if request.method =='POST':
        products.delete()
        return redirect('home')
    return render(request, "delete.html", context)


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class productreg(CreateView):
	model = product
	fields = '__all__'
	template_name = 'CBV/productreg.html'
	success_url ="/"
	
class productlist(ListView):
	model = product
	template_name = 'CBV/productlist.html'

class productdetail(DetailView):
	model =product
	template_name = 'CBV/productdetail.html'

class productupdate(UpdateView):
	model = product
	fields = "__all__"
	template_name = 'CBV/productupdate.html'
	success_url ="/"

class productdelete(DeleteView):
	model = product
	template_name = 'CBV/productdelete.html'
	success_url ="/"
