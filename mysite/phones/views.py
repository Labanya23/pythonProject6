from django.shortcuts import render
from .forms import PhoneForm

def add_product(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Phone_list')
        else:
            form = forms.PhoneForm()
            return render(request,'')

# Create your views here.
