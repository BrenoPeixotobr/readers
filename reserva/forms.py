from django import forms

from .models import Reserva


class PostReserva(forms.ModelForm):
    class Meta:
        model = Reserva
