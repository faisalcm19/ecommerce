from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from ecom.forms import UserRegister,UserLogin,CartForm,OdersForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from ecom.models import product,Carts,Oders
from django.core.mail import send_mail,settings


# Create your views here.


class HomeView(View):
    def get(self,request,*args,**kwargs):
        data=product.objects.all()
        return render(request,'index.html',{'products':data})
    
class UserRegisterView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegister()
        return render(request,'userRegister.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form=UserRegister(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'registrayion ok')
            return render(request,'userlogin.html')
        else:
            messages.error(request,'invalid')
            return redirect('home_view')


class UserLoginView(View):
    def get(self,request,*args,**kwargs):
        form=UserLogin()
        return render(request,'userlogin.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        usname=request.POST.get('username')
        psw=request.POST.get('password')
        user=authenticate(request,username=usname,password=psw)
        if user:
            login(request,user)
            messages.success(request,'login ok')
            return redirect('home_view')
        else:
            messages.error(request,'login fail')
            return redirect('login_view')  


class Userlogout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'logot sucess')
        return redirect('home_view')    

class ProductDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        id=product.objects.get(id=id)
        return render(request,'product.html',{'product':id})
    

class AddtoCart(View):
    def get(self,request,*args,**kwargs):
        form=CartForm()
        id=kwargs.get('id')
        prod=product.objects.get(id=id)
        return render(request,'addtocart.html',{'form':form,'product':prod})
    
    
    def post(self,request,*args,**kwargs):
        us=request.user
        id=kwargs.get('id')
        prod=product.objects.get(id=id)
        quanty=request.POST.get('quantity')
        Carts.objects.create(user=us,quantity=quanty,product=prod)
        return redirect('home_view')
    

class Cartlist(View):
    def get(self,request,*args,**kwargs):
        data=Carts.objects.filter(user=request.user).exclude(status='order-placed')
        print(data)
        return render(request,'cartlist.html',{'cart':data})
class Placeorderview(View):
    def get(self,request,*args,**kwargs):
        form=OdersForm()
        return render(request,'placeorder.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        cart_id=kwargs.get('cart_id')
        cart=Carts.objects.get(id=cart_id)
        user=request.user
        address=request.POST.get('address')
        email=request.POST.get('email')
        Oders.objects.create(user=user,carts=cart,address=address,email=email)
        send_mail("confirmation","order placed successfully!",settings.EMAIL_HOST_USER,[email])
        cart.status='order-placed'
        cart.save()
        return redirect('home_view')

class CartdeletView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('id')
        data=Carts.objects.get(id=id)
        data.delete()
        return redirect('cart_list')









