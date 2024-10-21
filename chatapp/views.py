from django.views.generic import ListView
from django.shortcuts import redirect,render
from django.urls import reverse
from .models import chat
from .forms import chatForm
from datetime import datetime

now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class chatView(ListView):
    model = chat
    template_name = 'myapp/chat.html'
    context_object_name = 'chats'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = chatForm()
        context['now_date'] = now_date
        return context

    def post(self, request, *args, **kwargs):
        form = chatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chat')
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data(object_list=self.object_list)
            context['form'] = form
            return self.render_to_response(context)