from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .forms import ResForm, MenuForm
from .models import Customers, Restarunts, Menu, Cart
from django.conf import settings
import razorpay
# Create your views here.

def index(request):
    return render(request, 'delivery/index.html')

def sign_in(request):
    return render(request, 'delivery/sign_in.html')

def sign_up(request):
    return render(request, 'delivery/sign_up.html')

def handle_signin(request):
    li = Restarunts.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            cus = Customers.objects.get(username = username, password = password)
            if username == 'admin':
                return render(request, 'delivery/success.html')
            else:
                return render(request, 'delivery/cusdisplay_res.html', {'username':username,'li':li})
        except:
            return render(request, 'delivery/Failed.html') 

def handle_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        try:
            cus = Customers.objects.get(username = username, password = password)
            return render(request,'delivery/sign_in.html')
        except:
            cus = Customers(username = username, password = password, email = email,mobile = mobile, address = address)
            cus.save()
            return render(request,'delivery/sign_in.html')
    else:
        return HttpResponse("Invalid Request")
    
def add_res(request):
    form = ResForm(request.POST or None)
    if form.is_valid():
        Res_name = request.POST.get('res_name')
        try:
            res = Restarunts.objects.get(res_name = Res_name)
        except:
            form.save()
            return redirect('delivery:display_res')
    return render(request, 'delivery/add_res.html',{'form':form})

def display_res(request):
    li = Restarunts.objects.all()
    return render(request, 'delivery/display_res.html',{'li':li})

def view_menu(request, id):
    res = Restarunts.objects.get(pk = id)
    menu = Menu.objects.filter(res = res)
    return render(request, 'delivery/menu.html', {'res': res, 'menu':menu})

def add_menu(request, id):
    res = get_object_or_404(Restarunts, id=id)  # Get the restaurant object

    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)  # Don't save yet
            menu_item.res = res  # ✅ Assign the restaurant
            menu_item.save()     # ✅ Now save
            return redirect('delivery:view_menu', id=id)
    else:
        form = MenuForm()

    return render(request, 'delivery/menu_form.html', {'form': form, 'res': res})

def delete_menu(request, id):
    item = get_object_or_404(Menu, pk=id)  # Will raise 404 if not found
    res_id = item.res.id
    item.delete()
    return redirect('delivery:view_menu', res_id)

def cusdisplay_res(request,username):
        customer = Customers.objects.get(username=username)
        li = Restarunts.objects.all()
        return render(request, 'delivery/cusdisplay_res.html',{'li':li, 'username':username})

def cusmenu(request, id, username):
    res = Restarunts.objects.get(pk = id)
    menu = Menu.objects.filter(res = res)
    return render(request, 'delivery/cusmenu.html', {'res': res, 'menu':menu, 'username': username})

def update_restarunt(request, id):
    res = get_object_or_404(Restarunts, id=id)
    form = ResForm(request.POST or None, instance=res)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('delivery:display_res')  # back to list

    return render(request, 'delivery/update_res.html', {'form': form, 'res': res})

def delete_restarunt(request, id):
    res = get_object_or_404(Restarunts, id=id)
    res.delete()
    return redirect('delivery:display_res')

def show_cart(request, username):
    customer = Customers.objects.get(username = username)
    cart = Cart.objects.filter(customer = customer).first()
    items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0
    return render(request, 'delivery/show_cart.html',{'items':items,'total_price':total_price,'username':username})

def add_cart(request,id,username):
    customer = Customers.objects.get(username = username)
    item = Menu.objects.get(pk=id)
    cart, created = Cart.objects.get_or_create(customer = customer)
    cart.items.add(item)
    messages.success(request,f"{item.item_name} added")
    return redirect('delivery:cusmenu', id = item.res.id,username=username)


def checkout(request, username):
    customer = Customers.objects.get(username = username)
    cart = Cart.objects.filter(customer = customer).first()
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'delivery/checkout.html',{'error':'Your cart is Empty'})

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    order_data = {
        'amount':int(total_price * 100),
        'currency':'INR',
        'payment_capture':'1',
    }
    order = client.order.create(data = order_data)
    return render(
        request, 'delivery/checkout.html',
        {'username':username,
        'cart_items':cart_items,
        'total_price':total_price,
        'razorpay_key_id':settings.RAZORPAY_KEY_ID,
        'order_id':order['id'],
        'amount':total_price,
        }
    )

def orders(request, username):
        customer = Customers.objects.get(username = username)
        cart = Cart.objects.filter(customer=customer).first()
        cart_items = cart.items.all() if cart else []
        total_price = cart.total_price() if cart else 0

        if cart:
            cart.items.clear()

        return render(request, 'delivery/orders.html',{
        'username':username,
        'cart_items':cart_items,
        'total_price':total_price,
        'customer':customer
        })