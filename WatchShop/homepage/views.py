from django.shortcuts import render,redirect
from .models import WatchesUploads,Wishlist,Cart,Watch_Review,CartItem
from .forms import UploadForm ,ReviewForm
from django.contrib.auth.decorators import login_required      


def home(request):
    watches = WatchesUploads.objects.all()
    context = {'watches_t': watches}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')


@login_required(login_url="/login")
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()
        
    return render(request,'upload.html', {'form': form})
    
# Create your views here.






#view product
from django.shortcuts import get_object_or_404
def product(request,id):
    product = get_object_or_404(WatchesUploads, id=id)
    review =  Watch_Review.objects.filter(product=product)
    return render(request, "product.html",{"product": product,"reviews":review})


#wishlist
@login_required(login_url="/login")
def add_wishlist(request,id):
    user = request.user
    product = WatchesUploads.objects.get(id=id)
    obj1 ,created = Wishlist.objects.get_or_create( user = user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')
@login_required(login_url="/login")
def wishlist(request):
    user = request.user
    wish_objcet = Wishlist.objects.get( user = user)
    return render(request,"wishlist.html",{"user_product":wish_objcet.products.all()})
@login_required(login_url="/login")
def remove_wish(request,id):
    product_re = WatchesUploads.objects.get(id=id)  
    wish_object =Wishlist.objects.get(user=request.user)
    wish_object.products.remove(product_re)
    return render(request,"wishlist.html",{"user_product":wish_object.products.all()})


#cart
@login_required(login_url="/login")
def add_cart(request,id):
    user_cart, created = Cart.objects.get_or_create(user = request.user)
    product = WatchesUploads.objects.get(id=id)
    cart_item ,created = CartItem.objects.get_or_create( user = user_cart, product = product )
    cart_item.product= product
    cart_item.save()
    return redirect('home')
@login_required(login_url="/login")
def cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_objcet = user_cart.cartitem_set.all()
    return render(request,"cart.html",{"user_product":cart_objcet})
@login_required(login_url="/login")
def remove_cart(request,id):
    product_re = WatchesUploads.objects.get(id=id)  
    cart_object =Cart.objects.get(user=request.user)
    cart_object.products.remove(product_re)
    return render(request,"cart.html",{"user_product":cart_object.products.all()})







# LOGIN
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,  login, logout

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = user_name, password = password)
            
            if user is not None:
                 login(request,user)
                 return redirect('home') 
            else:
                return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        
    return render(request,'login.html', {'form': form})

#SIGNUP
def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#LOGOUT

def logout_user(request):
    logout(request)
    return redirect('home')



#search
def search_watch(request):
    query = request.GET.get('q')
    results = WatchesUploads.objects.filter(name__icontains=query) if query else []  # Use WatchUploads model
    return render(request, 'search_results.html', {'results': results})

def product_detail(request, watch_id):
    product = get_object_or_404(WatchesUploads, id=watch_id)
    review =  Watch_Review.objects.filter(product=product)
    return render(request, 'product.html', {'product': product , "reviews":review})



@login_required
def product_detail(request, watch_id):
    product = get_object_or_404(WatchesUploads, id=watch_id)
    reviews = Watch_Review.objects.filter(product=product)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', watch_id=watch_id)
    else:
        form = ReviewForm()

    return render(request, 'product.html', {'product': product, 'reviews': reviews, 'form': form})
