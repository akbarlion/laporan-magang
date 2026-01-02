from django import forms
from .models import LaporanHarian

class LaporanHarianForm(forms.ModelForm):
    class Meta:
        model = LaporanHarian
        fields = ['tanggal', 'judul', 'kegiatan', 'kendala', 'rencana_besok', 'foto']
        widgets = {
            'tanggal': forms.DateInput(attrs={'type': 'date'}),
        }
