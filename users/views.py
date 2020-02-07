from django.shortcuts import render, redirect
from django.contrib import messages 
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Dept,BRs
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
@login_required
def timetablet(request):
	if request.user.profile.Department:
		tt = Dept.objects.filter(Dep = request.user.profile.Department).first()
		context = {
		'tt':tt
		}
		return render(request,'users/timetablet.html',context)
	return render(request,'users/timetablet.html')

class DeptUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Dept
    fields = ['D1P1','D1P2','D1P3','D1P4','D1P5','D1P6','D1P6','D1P7',
				'D2P1','D2P2','D2P3','D2P4','D2P5','D2P6','D2P6','D2P7',
				'D3P1','D3P2','D3P3','D3P4','D3P5','D3P6','D3P6','D3P7',
				'D4P1','D4P2','D4P3','D4P4','D4P5','D4P6','D4P6','D4P7',
				'D5P1','D5P2','D5P3','D5P4','D5P5','D5P6','D5P6','D5P7',
				'D6P1','D6P2','D6P3','D6P4','D6P5','D6P6','D6P6','D6P7']

    def form_valid(self, form):
        form.instance.Dep = self.request.user.profile.Department
        return super().form_valid(form)

    def test_func(self):
        dept = self.get_object()
        if self.request.user.profile.Roll_No == BRs.objects.filter(department = self.request.user.profile.Department ).first().roll_no:
            return True
        return False