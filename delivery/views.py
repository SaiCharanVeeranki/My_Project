from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .forms import ResForm, MenuForm
from .models import Customers, Restarunts, Menu
# Create your views here.

def index(request):
    return render(request, 'delivery/index.html')

def sign_in(request):
    return render(request, 'delivery/sign_in.html')

def sign_up(request):
    return render(request, 'delivery/sign_up.html')

def handle_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            cus = Customers.objects.get(username = username, password = password)
            if username == 'admin':
                return render(request, 'delivery/success.html')
            else:
                return render(request, 'delivery/customer_home.html')
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

def cusdisplay_res(request):
        li = Restarunts.objects.all()
        return render(request, 'delivery/cusdisplay_res.html',{'li':li})

def cusmenu(request, id):
    res = Restarunts.objects.get(pk = id)
    menu = Menu.objects.filter(res = res)
    return render(request, 'delivery/cusmenu.html', {'res': res, 'menu':menu})