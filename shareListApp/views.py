from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserloginForm,AddSharesForm
from .models import UserDetails,ShareDetails


# Create your views here.
def index(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('user_login')
    form = UserRegistrationForm()
    return render(request, 'sharelistapp/onboarding.html', {'form':form})

def userlogin(request):
    if request.method=="POST":
        form = UserloginForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            email1 = request.POST.get('email')
            password1 = request.POST.get('password')
            obj_list = UserDetails.objects.all().filter(email=email1,password=password1)
            name = 'Welcome, '
            for i in obj_list:
                name += f"{i.first_name} {i.last_name}"
            # print(name)
        for obj in obj_list:
            if obj.email==email1 and obj.password==password1:
                return redirect('user_list')
    login_form = UserloginForm()
    return render(request, 'sharelistapp/userlogin.html', {'form':login_form})

def userlist(request):
    dataobjs = UserDetails.objects.all()
    # print(dataobjs)
    return render(request, 'sharelistapp/userlist.html', {"data":dataobjs})

def shareslist(request,s_id=None,id=None):      

    if request.method=="POST" and id!=None:
        e_dop = request.POST.get('Inputdop')
        e_compname = request.POST.get('Inputcompname')
        e_price = request.POST.get('Inputprice')
        e_quantity = request.POST.get('Inputquantity')
            
        instances = ShareDetails.objects.all().filter(shareid=s_id)
        
        for instance in instances:
            print(f"ShareID: {instance.shareid}, DOP: {instance.dop}, company name: {instance.comp_name}, price: {instance.price}, quantity: {instance.quantity}, UserID: {instance.userid}")

        for instance in instances:
            # instance.comp_name = e_compname
            instance.price = e_price
            instance.quantity = e_quantity
            instance.save()

        for instance in instances:
            print(f"ShareID: {instance.shareid}, DOP: {instance.dop}, company name: {instance.comp_name}, price: {instance.price}, quantity: {instance.quantity}, UserID: {instance.userid}")

        return redirect('shares_list',id)

    if request.method == "GET" and id!=None:
        dataobjs = ShareDetails.objects.all().filter(userid=id).order_by('-dop').values()
        return render(request, 'sharelistapp/shareslist.html', {"data":dataobjs,'id':id})
        
def addshares(request,id=None):
    if request.method=="POST" and id!=None:
        form = AddSharesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.cleaned_data['userid']=id
            print(form.cleaned_data)
            # print('shares added...')
            form.save()
            return redirect('shares_list',id)
    addsharesform = AddSharesForm()
    return render(request, 'sharelistapp/addshares.html',{'form':addsharesform})

def deleteshare(request, s_id=None,id=None):
    if request.method == "GET" and id!=None:
        obj = ShareDetails.objects.all().filter(shareid=s_id,userid=id)
        obj.delete()
        return redirect('shares_list',id)
        