from django.shortcuts import render, redirect
from .models import Photographer,Photo,Bookings
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

def is_user(user):
    if not user.is_anonymous:
        name = user.get_short_name()
        admin_name=Photographer.objects.filter(name=name)
        if admin_name:
            return False
        else:
            return True
    else:
        return False

def is_member(user):
    if not user.is_anonymous:
        name = user.get_short_name()
        admin_name=Photographer.objects.filter(name=name)
        if admin_name:
            return True
        else:
            return False
    else:
        return False


def RegisterUser(request):
    page='register'
    if request.method=='POST':
        first_name=request.POST.get('name')
        username=request.POST.get('username')
        mail_id=request.POST.get('mail_id').lower()
        passwd=request.POST.get('confirm-password') 
        user = User.objects.create_user(first_name=first_name,username=username,email=mail_id,password=passwd)
        user.save()
        login(request,user)
        return redirect ('home')

    context={'page':page}
    return render(request, 'authenticate.html',context)

def LoginAdmin(request):
    page='adminlogin'
    if request.method=='POST':
        mail_id=request.POST.get('loginmail_id').lower()
        password=request.POST.get('loginpasswd')
        try:
                    user=User.objects.get(email=mail_id)
                    username=user.get_username()
        except:
                    messages.error(request, 'User Doesn\'t Exist ')
                    return redirect('login')
        user=authenticate(username=username,password=password)

        if user is not None:
                login(request,user)
                return redirect('portfolios')
        else:
            messages.error(request, 'Password Incorrect')
            return redirect('login')
    context={'page':page}
    return render(request, 'authenticate.html',context) 

def LoginUser(request):
    page='login'
    if request.method=='POST':
        mail_id=request.POST.get('loginmail_id').lower()
        password=request.POST.get('loginpasswd')
        try:
                    user=User.objects.get(email=mail_id)
                    username=user.get_username()
        except:
                    messages.error(request, 'User Doesn\'t Exist ')
                    return redirect('login')
        user=authenticate(username=username,password=password)

        if user is not None:
                login(request,user)
                return redirect('portfolios')
        else:
            messages.error(request, 'Password Incorrect')
            return redirect('login')
    context={'page':page}
    return render(request, 'authenticate.html',context) 

def LogoutUser(request):
    global AdminStatus
    logout(request)
    AdminStatus=False
    return redirect('home')

def HomePage(requests):
    return render(requests,'home.html')

def Portfolios(requests):
    photographer=requests.GET.get('photographer')
    if photographer == None:
        photos = Photo.objects.all()
    else:
        photos= Photo.objects.filter(photographer__name = photographer)
    photographers = Photographer.objects.all()
    

    context={'photographers':photographers,'photos':photos}
    return render(requests,'portfolios.html',context)


def ViewPhoto(requests,pk):
    photo = Photo.objects.get(id=pk)
    return render(requests,'download.html',{'photo':photo})

@user_passes_test(is_member,login_url='adminlogin')
def AddPhoto(requests):
        photographers = Photographer.objects.all()
        if requests.method =='POST':
            data= requests.POST
            image= requests.FILES.get('image')

            if data['photographer']!='none':
                photographer= Photographer.objects.get(id=data['photographer'])
            else:
                photographer= None

            photo = Photo.objects.create(
                photographer=photographer,
                description= data['description'],
                image=image,
            )
            return redirect('portfolios')
        context={'photographers':photographers}
        return render(requests,'addphoto.html',context)



def TestimonialsPage(requests):
    return render(requests,'testimonials.html')

@login_required(login_url='login')
@user_passes_test(is_user,login_url='login')
def Booking(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        photographer=request.POST.get('booking')
        booking_date=request.POST.get('date')
        booking_time=request.POST.get('time')
        booking_hours=request.POST.get('hours')
        booking=Bookings(name=name,email=email,address=address,photographer=photographer,booking_date=booking_date,booking_time=booking_time,booking_hours=booking_hours)
        booking.save()
        if booking:
            return redirect('portfolios')
    return render(request,'bookings.html')

