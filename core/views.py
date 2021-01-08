from django.shortcuts import render,HttpResponseRedirect
from .forms import StuRegis
from .models import User
# Create your views here.

#==================================Add & Delete Record=======================================================================#
def index(req):
    All_user = User.objects.all()
    if req.method == 'POST':
        frm = StuRegis(req.POST)
        if frm.is_valid():
            frm.save()
            # name = frm.cleaned_data['name']
            # email = frm.cleaned_data['email']
            # password = frm.cleaned_data['password']
            # saveUser = User(name = name , email = email, password = password)
            # saveUser.save()
            frm = StuRegis()

    else:
        frm = StuRegis()
    return render(req,'core/index.htm',{"form":frm,"all_user":All_user})

#==================================Add & Delete Record=======================================================================#

def DeleteRec(req):
    if req.method == 'POST':
        id = req.POST.get('delId')
        pd = User.objects.get(pk=id)
        pd.delete()
    return HttpResponseRedirect('/')


def Details(req,edit_id):
    pd = User.objects.get(pk=edit_id)
    if req.method == 'POST':
        fm = StuRegis(req.POST,instance=pd)
        if fm.is_valid():
            fm.save()
    else:
        fm = StuRegis(instance=pd)
    return render(req,'core/detail.htm',{"Frm":fm})

