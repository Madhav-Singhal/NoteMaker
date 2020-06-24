from django.shortcuts import render, redirect, get_object_or_404
from .models import Create
from .forms import Create_form, UserForm
from django.contrib.auth.models import User, auth



def login(request):
    if request.method == 'POST':
        val3 = request.POST['username']
        val4 = request.POST['password']

        user = auth.authenticate(username=val3, password=val4)

        if user is not None:
            auth.login(request, user)
            return redirect("notesapp:list")
        else:
            return redirect('notesapp:login')

    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        val1 = request.POST['first_name']
        val2 = request.POST['last_name']
        val3 = request.POST['username']
        val4 = request.POST['password']
        val5 = request.POST['confirm']

        if val4 == val5:
            if User.objects.filter(username=val3).exists():
                
                
                return render(request, 'register.html')
            else:


                user = User.objects.create_user(username = val3, password = val4, first_name = val1, last_name = val2)
                user.save()
                return redirect("notesapp:login")

        else:
            return redirect('notesapp:register')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
            



def list(request):
    if not request.user.is_authenticated:
        return redirect('notesapp:login')

    obj = Create.objects.all().filter(user=request.user)
    user = ((request.user.first_name).lower()).capitalize() + ' ' + ((request.user.last_name).lower()).capitalize()
    count = obj.count()
    return render(request, 'list.html', {'object':obj, 
                                             'c': count, 'user':user})


def create(request):

    if not request.user.is_authenticated:
        return redirect('notesapp:login')

    my_form = Create_form
    if request.method == 'POST':
        my_form = Create_form(request.POST or None)
        if my_form.is_valid():

            form =my_form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect("notesapp:list")
             
    return render(request, 'create.html', {'form': my_form})

 

def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('notesapp:login')

    y = Create.objects.get(pk = id)

    if y.user == request.user:
        y.delete()
        return redirect('notesapp:list')
    else:
        return redirect('notesapp:list')



def edit(request, id):
    if not request.user.is_authenticated:
        return redirect('notesapp:login')


    update_obj = get_object_or_404(Create, id = id)
    if update_obj.user == request.user:
        form = Create_form(request.POST or None, request.FILES or None, instance = update_obj)
        if form.is_valid():
            
            form.save()
            
            return redirect("notesapp:list")
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)

    else:
        return redirect("notesapp:list")

