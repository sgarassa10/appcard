from django.conf import settings 
from django.db import models 
from django.utils import timezone 

# Create your models here.

class Tipologie(models.Model):
    """ il modello generico di un giornalista """
    descrizione = models.CharField(max_length=20)
    note = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.descrizione + " " + self.note

    class Meta:
        # link utile : https://docs.djangoproject.com/en/2.0/ref/models/options/
        verbose_name = "Tipologia"
        verbose_name_plural = "Tipologie"



class Fornitori(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ragsoc = models.CharField(max_length=100, verbose_name="Ragione sociale")
    piva = models.CharField(max_length=16, verbose_name="Partita iva")
    codfisc = models.CharField(max_length=16, verbose_name="Codice fiscale")
    indleg = models.CharField(max_length=80, verbose_name="Indirizzo sede legale")
    cittaleg = models.CharField(max_length=50, verbose_name="Città sede legale")
    prleg = models.CharField(max_length=2, verbose_name="Provincia sede legale")
    indatt = models.CharField(null = True, blank=True, max_length=80, verbose_name="Indirizzo attività")
    cittaatt = models.CharField(null = True, blank=True, max_length=50, verbose_name="Città attività")
    pratt = models.CharField(null = True, blank=True, max_length=2, verbose_name="Provincia attività")
    telefono = models.CharField(null = True, blank=True, max_length=16, verbose_name="Telefono")
    cellulare = models.CharField(null = True, blank=True, max_length=16, verbose_name="Mobile")
    email = models.EmailField(null = True, blank=True, max_length=80, verbose_name="E-mail")
    emailpec = models.EmailField(null = True, blank=True, max_length=80, verbose_name="E-mail pec")
    indwb = models.URLField(null = True, blank=True, max_length=50, verbose_name="Indirizzo web")
    sdi = models.CharField(null = True, blank=True, max_length=7, verbose_name="Codice SDI")
    coordgps = models.CharField(null = True, blank=True, max_length=20, verbose_name="Coordinate GPS")
    tipologia = models.ForeignKey(Tipologie, on_delete=models.CASCADE, verbose_name="Tipo attività")
    referente = models.CharField(null = True, blank=True, max_length=50, verbose_name="Referente")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data creazione")

    def __str__(self):
        return self.ragsoc

    class Meta:        
        verbose_name = "Fornitore"
        verbose_name_plural = "Fornitori"


class SedeFornitori(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fornit = models.ForeignKey(Fornitori, on_delete=models.CASCADE, verbose_name="Fornitore")
    insegna = models.CharField(max_length=50, verbose_name="Denominazione")
    indirizzo = models.CharField(max_length=80, verbose_name="Indirizzo")
    citta = models.CharField(max_length=50, verbose_name="Città")
    pr = models.CharField(max_length=2, verbose_name="Provincia")
    telefono = models.CharField(null = True, blank=True, max_length=16, verbose_name="Telefono")
    cellulare = models.CharField(null = True, blank=True, max_length=16, verbose_name="Mobile")
    email = models.EmailField(null = True, blank=True, max_length=80, verbose_name="E-mail")
    emailpec = models.EmailField(null = True, blank=True, max_length=80, verbose_name="E-mail pec")
    indwb = models.URLField(null = True, blank=True, max_length=50, verbose_name="Indirizzo web")
    tipologia = models.ForeignKey(Tipologie, on_delete=models.CASCADE, verbose_name="Tipo attività")
    mqstruttura = models.CharField(null = True, blank=True, max_length=7, verbose_name="Mq struttura")
    numloc = models.IntegerField(null = True, verbose_name="Numero Locali")
    tipologia = models.ForeignKey(Tipologie, on_delete=models.CASCADE, verbose_name="Tipo attività")
    referente = models.CharField(null = True, blank=True, max_length=50, verbose_name="Referente")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data creazione")

    def __str__(self):
        return self.fornit

    class Meta:        
        verbose_name = "Sede Fornitore"
        verbose_name_plural = "Sedi Fornitori"


class DocFornitore(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fornit = models.ForeignKey(Fornitori, on_delete=models.CASCADE, verbose_name="Fornitore")
    sede = models.ForeignKey(SedeFornitori, on_delete=models.CASCADE, null = True, blank=True, verbose_name="Sede")
    documento = models.FileField(upload_to = "%Y/%m/%d")
    descrizione = models.CharField(null = True, max_length=50, verbose_name="Descrizione")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data creazione")

    def __str__(self):
        return self.fornit + " " + self.sede + " " + self.documento

    class Meta:        
        verbose_name = "Documentazione Fornitore"
        verbose_name_plural = "Documentazione Fornitore"



class Esperienze(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fornit = models.ForeignKey(Fornitori, on_delete=models.CASCADE, verbose_name="Fornitore")
    sede = models.ForeignKey(SedeFornitori, on_delete=models.CASCADE, null = True, blank=True, verbose_name="Sede")
    descrizione = models.CharField(max_length=30, verbose_name="Descrizione")
    descrizioneest = models.CharField(null = True, blank = True, max_length=200, verbose_name="Descrizione Estesa")
    referente = models.CharField(null = True, blank=True, max_length=50, verbose_name="Referente")
    prezzo_adulti = models.DecimalField(max_digits = 6, decimal_places = 3, verbose_name="Prezzo Adulti")
    etamaxbimbi = models.IntegerField(verbose_name="Età massima bambini")
    prezzo_bambini = models.DecimalField(max_digits = 6, decimal_places = 3, verbose_name="Prezzo Bambini")
    iva = models.IntegerField(verbose_name="Iva % applicata")
    durata = models.IntegerField(verbose_name="Durata Esperienza")
    minpart = models.IntegerField(verbose_name="Num minimo partecipanti")
    maxpart = models.IntegerField(verbose_name="Num massimo partecipanti")


    def __str__(self):
        return self.fornit + " " + self.sede + " " + self.descrizione

    class Meta:        
        verbose_name = "Esperienze"
        verbose_name_plural = "Esperienze"



class Gallery(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fornit = models.ForeignKey(Fornitori, on_delete=models.CASCADE, verbose_name="Fornitore")
    sede = models.ForeignKey(SedeFornitori, on_delete=models.CASCADE, null = True, blank=True, verbose_name="Sede")
    esperienza = models.ForeignKey(Esperienze, on_delete=models.CASCADE, verbose_name="Esperienza")
    upload_path = 'media/product'
    image = models.ImageField(upload_to=upload_path)
    descrizione = models.CharField(null = True, max_length=50, verbose_name="Descrizione")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data creazione")

    def __str__(self):
        return self.fornit + " " + self.sede + " " + self.descrizione

    class Meta:        
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"




class TipoCard(models.Model):
    descrizione = models.CharField(max_length=50, verbose_name="Descrizione")
    qtada = models.IntegerField(null = True, default=0, verbose_name="Q.tà a partire da")
    qtafinoa = models.IntegerField(null = True, default=0, verbose_name="Q.tà fino a")
    prezzo = models.DecimalField(max_digits = 6, decimal_places = 3, verbose_name="Prezzo")
    iva = models.IntegerField(verbose_name="Iva % applicata")
    nesperienze = models.IntegerField(verbose_name="Num max espereinze")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data creazione")

    def __str__(self):
        return self.descrizione 

    class Meta:        
        verbose_name = "Tipologia card"
        verbose_name_plural = "Tipologia card"


class Rivenditori(models.Model):
    ragsoc = models.CharField(null = True, blank=True, max_length=80, verbose_name="Ragione Sociale")
    indirizzo = models.CharField(max_length=80, verbose_name="Indirizzo")
    citta = models.CharField(max_length=50, verbose_name="Città")
    pr = models.CharField(max_length=2, verbose_name="Provincia")
    telefono = models.CharField(null = True, blank=True, max_length=16, verbose_name="Telefono")
    cellulare = models.CharField(null = True, blank=True, max_length=16, verbose_name="Mobile")
    email = models.EmailField(null = True, blank=True, max_length=80, verbose_name="E-mail")
    emailpec = models.EmailField(null = True, blank=True, max_length=80, verbose_name="E-mail pec")
    piva = models.CharField(null = True, blank=True, max_length=16, verbose_name="Partita iva")
    codfisc = models.CharField(max_length=16, verbose_name="Codice fiscale")    
    indwb = models.URLField(null = True, blank=True, max_length=50, verbose_name="Indirizzo web")
    sdi = models.CharField(null = True, blank=True, max_length=7, verbose_name="Codice SDI")
    coordgps = models.CharField(null = True, blank=True, max_length=20, verbose_name="Coordinate GPS")
    tipologia = models.ForeignKey(Tipologie, on_delete=models.CASCADE, verbose_name="Tipo attività")
    referente = models.CharField(null = True, blank=True, max_length=50, verbose_name="Referente")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data creazione")

    def __str__(self):
        return self.ragsoc

    class Meta:        
        verbose_name = "Rivenditore"
        verbose_name_plural = "Rivenditori"




class AquistoCard(models.Model):
    dataacquisto = models.DateTimeField(default=timezone.now, verbose_name="Data acquisto")
    rivenditore = models.ForeignKey(Rivenditori, on_delete=models.CASCADE, verbose_name="Rivenditore")
    TipoCard = models.ForeignKey(TipoCard, on_delete=models.CASCADE, verbose_name="Tipologia card")
    qta = models.IntegerField(default=0, verbose_name="Q.tà")
    prezzo = models.DecimalField(max_digits = 6, decimal_places = 3, verbose_name="Prezzo")
    iva = models.IntegerField(verbose_name="Iva % applicata")
    totriga  = models.DecimalField(max_digits = 6, decimal_places = 3, verbose_name="Totale riga")
    descrizione = models.CharField(max_length=50, verbose_name="Descrizione")

    def __str__(self):
        return self.dataacquisto + " " + self.rivenditore

    class Meta:        
        verbose_name = "Acquisto card"
        verbose_name_plural = "Acquisto card"




class LottiAquistoCard(models.Model):
    rifacquisto = models.ForeignKey(AquistoCard, on_delete=models.CASCADE, verbose_name="Rif acquisto")
    Numcard = models.IntegerField(verbose_name="Numero card")
    qrcode = models.CharField(max_length=50,  verbose_name="Qr Code")
    qta = models.IntegerField(default=1, verbose_name="Q.tà")


    def __str__(self):
        return self.rifacquisto + " " + self.rivenditore

    class Meta:        
        verbose_name = "Lotto d'acquisto card"
        verbose_name_plural = "Lotto d'acquisto card"




class Clienti(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    cognome = models.CharField(max_length=80, verbose_name="Cognome")
    denominazione = models.CharField(null = True, blank=True, max_length=80, verbose_name="Ragione Sociale")
    indirizzo = models.CharField(max_length=80, verbose_name="Indirizzo")
    citta = models.CharField(max_length=50, verbose_name="Città")
    pr = models.CharField(max_length=2, verbose_name="Provincia")
    telefono = models.CharField(null = True, blank=True, max_length=16, verbose_name="Telefono")
    cellulare = models.CharField(null = True, blank=True, max_length=16, verbose_name="Mobile")
    email = models.EmailField(null = True, blank=True, max_length=80, verbose_name="E-mail")
    piva = models.CharField(null = True, blank=True, max_length=16, verbose_name="Partita iva")
    codfisc = models.CharField(max_length=16, verbose_name="Codice fiscale")    
    numadulti = models.IntegerField(null = True, verbose_name="Numero Adulti nucleo familiare")
    numabimbimax3 = models.IntegerField(null = True, default=0, verbose_name="Numero Bambini nucleo familiare <= 3 anni")
    numabimbimin3 = models.IntegerField(null = True, default=0, verbose_name="Numero Bambini nucleo familiare > 3 anni")
    qrcodecard = models.ForeignKey(LottiAquistoCard, on_delete=models.CASCADE, verbose_name="Qr Code")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data creazione")

    def __str__(self):
        return self.nome + " " + self.cognome

    class Meta:        
        verbose_name = "Cliente"
        verbose_name_plural = "Cienti"



WEEKDAYS = [
    (1, ("Lunedi")),
    (2, ("Martedi")),
    (3, ("Mercoledi")),
    (4, ("Giovedi")),
    (5, ("Venerdi")),
    (6, ("Sabato")),
    (7, ("Domenica")),
 ]
class RegoleAgendaAperture(models.Model):

    TI01_weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True, verbose_name='Giorno')
    TI01_from_houram = models.TimeField(verbose_name='dalle ore am')
    TI01_to_houram = models.TimeField(verbose_name='alle ore am')
    TI01_from_hourpm = models.TimeField(verbose_name='dalle ore pm')
    TI01_to_hourpm = models.TimeField(verbose_name='alle ore pm')
    def __str__(self):
            return str(self.TI01_weekday)
    class Meta:
            verbose_name_plural = 'Orari e giorni disponibilità'



class RegoleEsclusioniAgenda(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fornit = models.ForeignKey(Fornitori, on_delete=models.CASCADE, verbose_name="Fornitore")
    sede = models.ForeignKey(SedeFornitori, on_delete=models.CASCADE, null = True, blank=True, verbose_name="Sede")
    esperienza = models.ForeignKey(Esperienze, on_delete=models.CASCADE, verbose_name="Esperienza")
    data_esclusione = models.DateTimeField(verbose_name="Data inizio disponibilità")

    def __str__(self):
        return self.fornit + " " + self.esperienza

    class Meta:        
        verbose_name = "Regole Esclusioni Agenda"
        verbose_name_plural = "Regole Esclusioni Agenda"



class RegoleAgenda(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fornit = models.ForeignKey(Fornitori, on_delete=models.CASCADE, verbose_name="Fornitore")
    sede = models.ForeignKey(SedeFornitori, on_delete=models.CASCADE, null = True, blank=True, verbose_name="Sede")
    esperienza = models.ForeignKey(Esperienze, on_delete=models.CASCADE, verbose_name="Esperienza")
    data_inizio = models.DateTimeField(default=timezone.now, verbose_name="Data inizio disponibilità")
    data_fine = models.DateTimeField(verbose_name="Data fine disponibilità")
    giorni = models.ManyToManyField(RegoleAgendaAperture, verbose_name='Giorni disponibilità')
    giorni_esclusione = models.ManyToManyField(RegoleEsclusioniAgenda, verbose_name='Giorni anno non disponibili')


    def __str__(self):
        return self.fornit + " " + self.esperienza

    class Meta:        
        verbose_name = "Regole Agenda"
        verbose_name_plural = "Regole Agenda"



