from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, UpdateView


# Create your views here.
from .models import LineOfScript


def sound_home_view(request, *args, **kwargs):
    content = {

        'line_actual': LineOfScript.objects.all()
    }

    return render(request, 'sound.html', content)


def edit_note(request, *args, **kwargs):
    pk = request.GET("pk")

    content = {
        "form"
    }
    return render(request, 'edit_note.html', content)

class ScriptList(ListView):
    model = LineOfScript
    context_object_name = "line_actual"
    queryset = LineOfScript.objects.all()
    template_name = "sound.html"

class ScriptUpdate(UpdateView):
    model = LineOfScript
    fields = ["note_description", "highlight"]
    template_name = "edit_note.html"
    success_url =  '/'
