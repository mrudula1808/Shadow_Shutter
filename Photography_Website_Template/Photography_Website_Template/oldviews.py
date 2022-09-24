# from django.shortcuts import render, redirect
# from .models import Photographer,Photo,Bookings,admin
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate, logout
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required


# def AdminLogin(request):
#     if request.method=='POST':
#         global Admin
#         global AdminStatus
#         mail_id=request.POST.get('admin_mail_id')
#         password=request.POST.get('adminpasswd')
#         try:
#             adminuser=admin.objects.filter(email=mail_id)
#         except:
#             messages.error(request,'Admin Doesn\'t exist')
#         if adminuser:
#             ExistingMail=admin.objects.filter(email__iexact=mail_id)
#             Existingpassword=admin.objects.get(password__exact=password)
#             print(ExistingMail,Existingpassword)
#             if ExistingMail and Existingpassword:
#                 Admin='True'
#                 AdminStatus='True'
#                 messages.success(request,'Welcome Admin')
#                 return redirect('portfolios')
#             else:
#                 Admin='False'
#                 AdminStatus='False'
#                 messages.error(request,'Invalid Credentials') 
#     context={'AdminStatus':AdminStatus}
#     return render(request, 'adminlogin.html',context)
        



# def RegisterUser(request):
#     page='register'
#     if request.method=='POST':
#         first_name=request.POST.get('name')
#         username=request.POST.get('username')
#         mail_id=request.POST.get('mail_id').lower()
#         passwd=request.POST.get('passwd') 
#         user = User.objects.create_user(first_name=first_name,username=username,email=mail_id,password=passwd)
#         user.save()
#         login(request,user)
#         return redirect ('home')

#     context={'page':page}
#     return render(request, 'authenticate.html',context)


# def LoginUser(request):
#     page='login'
#     if request.method=='POST':
#         mail_id=request.POST.get('loginmail_id').lower()
#         password=request.POST.get('loginpasswd')
#         try:
#                     user=User.objects.get(email=mail_id)
#                     username=user.get_username()
#         except:
#                     messages.error(request, 'User Doesn\'t Exist ')
#                     return redirect('login')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#                 login(request,user)
#                 return redirect('portfolios')
#         else:
#                 messages.error(request, 'Password Incorrect')
#                 return redirect('login')
#     context={'page':page}
#     return render(request, 'authenticate.html',context) 

# def LogoutUser(request):
#     global AdminStatus
#     logout(request)
#     AdminStatus=False
#     return redirect('home')

# def HomePage(requests):
#     return render(requests,'home.html')

# def Portfolios(requests):
#     photographer=requests.GET.get('photographer')
#     if photographer == None:
#         photos = Photo.objects.all()
#     else:
#         photos= Photo.objects.filter(photographer__name = photographer)
#     photographers = Photographer.objects.all()
    

#     context={'photographers':photographers,'photos':photos}
#     return render(requests,'portfolios.html',context)


# def ViewPhoto(requests,pk):
#     photo = Photo.objects.get(id=pk)
#     return render(requests,'download.html',{'photo':photo})
    
# def AddPhoto(requests):
#     if AdminStatus =='True':
#         photographers = Photographer.objects.all()
#         if requests.method =='POST':
#             data= requests.POST
#             image= requests.FILES.get('image')

#             if data['photographer']!='none':
#                 photographer= Photographer.objects.get(id=data['photographer'])
#             elif data['photographer_new']!='':
#                 photographer, created = Photographer.objects.get_or_create(name=data['photographer_new'])
#             else:
#                 photographer= None

#             photo = Photo.objects.create(
#                 photographer=photographer,
#                 description= data['description'],
#                 image=image,
#             )
#             return redirect('portfolios')
#         context={'photographers':photographers}
#         return render(requests,'addphoto.html',context)
#     else:
#         return redirect ('adminlogin')



# def TestimonialsPage(requests):
#     return render(requests,'testimonials.html')

# @login_required(login_url='login')
# def Booking(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         address=request.POST.get('address')
#         photographer=request.POST.get('booking')
#         booking_date=request.POST.get('date')
#         booking_time=request.POST.get('time')
#         booking_hours=request.POST.get('hours')
#         booking=Bookings(name=name,email=email,address=address,photographer=photographer,booking_date=booking_date,booking_time=booking_time,booking_hours=booking_hours)
#         booking.save()
#         if booking:
#             return redirect('portfolios')
#     return render(request,'bookings.html')