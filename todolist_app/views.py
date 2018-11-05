from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView, CreateView, DeleteView, ModelFormMixin, FormView
from django.views.generic.list import ListView

from todolist_app.forms import TodoModelForm
from todolist_app.models import Todo


class IndexView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('todolist_app:sign_in')
    queryset = Todo.objects.all()
    model = Todo
    template_name = 'todolist_app/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        sort = self.request.GET.get('sort', '-pub_date')

        if user.is_superuser:
            return queryset.order_by(sort)

        return queryset.filter(user=user).order_by(sort)


class TodoDetailView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoModelForm
    template_name_suffix = '_detail_form'
    success_url = reverse_lazy('todolist_app:index')


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('todolist_app:index')


class TodoCreateView(CreateView, ModelFormMixin):
    model = Todo
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('todolist_app:index')
    form_class = TodoModelForm
    request = None

    def get_initial(self):
        init = super(TodoCreateView, self).get_initial()
        init.update({
            'user': self.request.user
        })
        return init


class SignUpFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('todolist_app:sign_in')
    template_name = "todolist_app/sign_up.html"

    def form_valid(self, form):
        form.save()
        return super(SignUpFormView, self).form_valid(form)


class SignInFormView(FormView):
    form_class = AuthenticationForm
    template_name = "todolist_app/sign_in.html"
    success_url = reverse_lazy('todolist_app:index')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(SignInFormView, self).form_valid(form)


class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/todolist_app")
