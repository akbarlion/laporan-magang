from django.db import models

class LaporanHarian(models.Model):
    tanggal = models.DateField()
    hari = models.CharField(max_length=20, blank=True)
    tahun = models.PositiveIntegerField(blank=True, null=True)

    judul = models.CharField(max_length=120)
    kegiatan = models.TextField()
    kendala = models.TextField(blank=True)
    rencana_besok = models.TextField(blank=True)

    foto = models.ImageField(upload_to='laporan_foto/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-tanggal', '-created_at']

    def save(self, *args, **kwargs):
        if self.tanggal:
            hari_map = {
                "Monday":"Senin", "Tuesday":"Selasa", "Wednesday":"Rabu",
                "Thursday":"Kamis", "Friday":"Jumat", "Saturday":"Sabtu", "Sunday":"Minggu"
            }
            self.hari = hari_map.get(self.tanggal.strftime('%A'), self.tanggal.strftime('%A'))
            self.tahun = self.tanggal.year
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tanggal} - {self.judul}"
