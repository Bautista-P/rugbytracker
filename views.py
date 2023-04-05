from django.shortcuts import render, get_object_or_404, redirect
from .models import Jugador

def tackles(request):
    jugadores = Jugador.objects.all()
    context = {
        'jugadores': jugadores
    }
    return render(request, 'jugadores/tackles.html', context)

def increment_tackles(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    jugador.tackles += 1
    jugador.save()
    return redirect('jugadores:tackles')

def decrement_tackles(request, jugador_id):
    jugador = get_object_or_404(Jugador, pk=jugador_id)
    jugador.tackles -= 1
    jugador.save()
    return redirect('jugadores:tackles')

# Create your views here.
