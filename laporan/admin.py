from django.contrib import admin
from .models import LaporanHarian

@admin.register(LaporanHarian)
class LaporanHarianAdmin(admin.ModelAdmin):
    list_display = ('tanggal', 'hari', 'tahun', 'judul', 'created_at')
    list_filter = ('tahun', 'hari', 'tanggal')
    search_fields = ('judul', 'kegiatan', 'kendala', 'rencana_besok')
