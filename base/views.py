from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Assignment


class MySignInView(LoginView):
    template_name= 'base/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('assignments')


class SignUp(FormView):
    template_name = 'base/signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('assignments')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(SignUp, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('assignments')
        return super(SignUp, self).get(*args, **kwargs)


class AssignmentList(LoginRequiredMixin, ListView):
    model= Assignment
    context_object_name = 'assignments'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['assignments'] = context['assignments'].filter(user= self.request.user)
        context['count'] = context['assignments'].filter(complete= False).count()

        search_input= self.request.GET.get('search-area') or ''
        if search_input:
            context['assignments']= context['assignments'].filter(title__icontains=search_input)

        context['search_input'] = search_input

        return context


class AssignmentDetail(LoginRequiredMixin, DetailView):
    model = Assignment
    context_object_name= 'assignment'
    template_name= 'base/assignment.html'


class CreateAssignment(LoginRequiredMixin, CreateView):
    model = Assignment
    fields = [
        'title', 
        'description', 
        'complete',
        'due_date'
    ]
    success_url = reverse_lazy('assignments')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateAssignment, self).form_valid(form)


class UpdateAssignment(LoginRequiredMixin, UpdateView):
    model = Assignment
    fields = [
        'title', 
        'description', 
        'complete',
        'due_date'
    ]
    success_url = reverse_lazy('assignments')


class DeleteAssignment(LoginRequiredMixin, DeleteView):
    model= Assignment
    context_object_name= 'assignment'
    success_url = reverse_lazy('assignments')
