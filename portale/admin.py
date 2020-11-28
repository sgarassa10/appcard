from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Tipologie)
admin.site.register(Fornitori)
admin.site.register(SedeFornitori)
admin.site.register(DocFornitore)
admin.site.register(Esperienze)
admin.site.register(Gallery)
admin.site.register(TipoCard)
admin.site.register(Rivenditori)
admin.site.register(AquistoCard)
admin.site.register(LottiAquistoCard)
admin.site.register(Clienti)
admin.site.register(RegoleAgendaAperture)
admin.site.register(RegoleEsclusioniAgenda)
admin.site.register(RegoleAgenda)


