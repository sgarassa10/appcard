# Generated by Django 3.1.3 on 2020-11-26 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AquistoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataacquisto', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data acquisto')),
                ('qta', models.IntegerField(default=0, verbose_name='Q.tà')),
                ('prezzo', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Prezzo')),
                ('iva', models.IntegerField(verbose_name='Iva % applicata')),
                ('totriga', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Totale riga')),
                ('descrizione', models.CharField(max_length=50, verbose_name='Descrizione')),
            ],
            options={
                'verbose_name': 'Acquisto card',
                'verbose_name_plural': 'Acquisto card',
            },
        ),
        migrations.CreateModel(
            name='Esperienze',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=30, verbose_name='Descrizione')),
                ('descrizioneest', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrizione Estesa')),
                ('referente', models.CharField(blank=True, max_length=50, null=True, verbose_name='Referente')),
                ('prezzo_adulti', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Prezzo Adulti')),
                ('etamaxbimbi', models.IntegerField(verbose_name='Età massima bambini')),
                ('prezzo_bambini', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Prezzo Bambini')),
                ('iva', models.IntegerField(verbose_name='Iva % applicata')),
                ('durata', models.IntegerField(verbose_name='Durata Esperienza')),
                ('minpart', models.IntegerField(verbose_name='Num minimo partecipanti')),
                ('maxpart', models.IntegerField(verbose_name='Num massimo partecipanti')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Esperienze',
                'verbose_name_plural': 'Esperienze',
            },
        ),
        migrations.CreateModel(
            name='Fornitori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ragsoc', models.CharField(max_length=100, verbose_name='Ragione sociale')),
                ('piva', models.CharField(max_length=16, verbose_name='Partita iva')),
                ('codfisc', models.CharField(max_length=16, verbose_name='Codice fiscale')),
                ('indleg', models.CharField(max_length=80, verbose_name='Indirizzo sede legale')),
                ('cittaleg', models.CharField(max_length=50, verbose_name='Città sede legale')),
                ('prleg', models.CharField(max_length=2, verbose_name='Provincia sede legale')),
                ('indatt', models.CharField(blank=True, max_length=80, null=True, verbose_name='Indirizzo attività')),
                ('cittaatt', models.CharField(blank=True, max_length=50, null=True, verbose_name='Città attività')),
                ('pratt', models.CharField(blank=True, max_length=2, null=True, verbose_name='Provincia attività')),
                ('telefono', models.CharField(blank=True, max_length=16, null=True, verbose_name='Telefono')),
                ('cellulare', models.CharField(blank=True, max_length=16, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail')),
                ('emailpec', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail pec')),
                ('indwb', models.URLField(blank=True, max_length=50, null=True, verbose_name='Indirizzo web')),
                ('sdi', models.CharField(blank=True, max_length=7, null=True, verbose_name='Codice SDI')),
                ('coordgps', models.CharField(blank=True, max_length=20, null=True, verbose_name='Coordinate GPS')),
                ('referente', models.CharField(blank=True, max_length=50, null=True, verbose_name='Referente')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data creazione')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fornitore',
                'verbose_name_plural': 'Fornitori',
            },
        ),
        migrations.CreateModel(
            name='RegoleAgendaAperture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TI01_weekday', models.IntegerField(choices=[(1, 'Lunedi'), (2, 'Martedi'), (3, 'Mercoledi'), (4, 'Giovedi'), (5, 'Venerdi'), (6, 'Sabato'), (7, 'Domenica')], unique=True, verbose_name='Giorno')),
                ('TI01_from_houram', models.TimeField(verbose_name='dalle ore am')),
                ('TI01_to_houram', models.TimeField(verbose_name='alle ore am')),
                ('TI01_from_hourpm', models.TimeField(verbose_name='dalle ore pm')),
                ('TI01_to_hourpm', models.TimeField(verbose_name='alle ore pm')),
            ],
            options={
                'verbose_name_plural': 'Orari e giorni disponibilità',
            },
        ),
        migrations.CreateModel(
            name='TipoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=50, verbose_name='Descrizione')),
                ('qtada', models.IntegerField(default=0, null=True, verbose_name='Q.tà a partire da')),
                ('qtafinoa', models.IntegerField(default=0, null=True, verbose_name='Q.tà fino a')),
                ('prezzo', models.DecimalField(decimal_places=3, max_digits=6, verbose_name='Prezzo')),
                ('iva', models.IntegerField(verbose_name='Iva % applicata')),
                ('nesperienze', models.IntegerField(verbose_name='Num max espereinze')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data creazione')),
            ],
            options={
                'verbose_name': 'Tipologia card',
                'verbose_name_plural': 'Tipologia card',
            },
        ),
        migrations.CreateModel(
            name='Tipologie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=20)),
                ('note', models.CharField(max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Tipologia',
                'verbose_name_plural': 'Tipologie',
            },
        ),
        migrations.CreateModel(
            name='SedeFornitori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insegna', models.CharField(max_length=50, verbose_name='Denominazione')),
                ('indirizzo', models.CharField(max_length=80, verbose_name='Indirizzo')),
                ('citta', models.CharField(max_length=50, verbose_name='Città')),
                ('pr', models.CharField(max_length=2, verbose_name='Provincia')),
                ('telefono', models.CharField(blank=True, max_length=16, null=True, verbose_name='Telefono')),
                ('cellulare', models.CharField(blank=True, max_length=16, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail')),
                ('emailpec', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail pec')),
                ('indwb', models.URLField(blank=True, max_length=50, null=True, verbose_name='Indirizzo web')),
                ('mqstruttura', models.CharField(blank=True, max_length=7, null=True, verbose_name='Mq struttura')),
                ('numloc', models.IntegerField(null=True, verbose_name='Numero Locali')),
                ('referente', models.CharField(blank=True, max_length=50, null=True, verbose_name='Referente')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data creazione')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fornit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.fornitori', verbose_name='Fornitore')),
                ('tipologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.tipologie', verbose_name='Tipo attività')),
            ],
            options={
                'verbose_name': 'Sede Fornitore',
                'verbose_name_plural': 'Sedi Fornitori',
            },
        ),
        migrations.CreateModel(
            name='Rivenditori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ragsoc', models.CharField(blank=True, max_length=80, null=True, verbose_name='Ragione Sociale')),
                ('indirizzo', models.CharField(max_length=80, verbose_name='Indirizzo')),
                ('citta', models.CharField(max_length=50, verbose_name='Città')),
                ('pr', models.CharField(max_length=2, verbose_name='Provincia')),
                ('telefono', models.CharField(blank=True, max_length=16, null=True, verbose_name='Telefono')),
                ('cellulare', models.CharField(blank=True, max_length=16, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail')),
                ('emailpec', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail pec')),
                ('piva', models.CharField(blank=True, max_length=16, null=True, verbose_name='Partita iva')),
                ('codfisc', models.CharField(max_length=16, verbose_name='Codice fiscale')),
                ('indwb', models.URLField(blank=True, max_length=50, null=True, verbose_name='Indirizzo web')),
                ('sdi', models.CharField(blank=True, max_length=7, null=True, verbose_name='Codice SDI')),
                ('coordgps', models.CharField(blank=True, max_length=20, null=True, verbose_name='Coordinate GPS')),
                ('referente', models.CharField(blank=True, max_length=50, null=True, verbose_name='Referente')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data creazione')),
                ('tipologia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.tipologie', verbose_name='Tipo attività')),
            ],
            options={
                'verbose_name': 'Rivenditore',
                'verbose_name_plural': 'Rivenditori',
            },
        ),
        migrations.CreateModel(
            name='RegoleEsclusioniAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_esclusione', models.DateTimeField(verbose_name='Data inizio disponibilità')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('esperienza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.esperienze', verbose_name='Esperienza')),
                ('fornit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.fornitori', verbose_name='Fornitore')),
                ('sede', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portale.sedefornitori', verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Regole Esclusioni Agenda',
                'verbose_name_plural': 'Regole Esclusioni Agenda',
            },
        ),
        migrations.CreateModel(
            name='RegoleAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inizio', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data inizio disponibilità')),
                ('data_fine', models.DateTimeField(verbose_name='Data fine disponibilità')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('esperienza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.esperienze', verbose_name='Esperienza')),
                ('fornit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.fornitori', verbose_name='Fornitore')),
                ('giorni', models.ManyToManyField(to='portale.RegoleAgendaAperture', verbose_name='Giorni disponibilità')),
                ('giorni_esclusione', models.ManyToManyField(to='portale.RegoleEsclusioniAgenda', verbose_name='Giorni anno non disponibili')),
                ('sede', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portale.sedefornitori', verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Regole Agenda',
                'verbose_name_plural': 'Regole Agenda',
            },
        ),
        migrations.CreateModel(
            name='LottiAquistoCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Numcard', models.IntegerField(verbose_name='Numero card')),
                ('qrcode', models.CharField(max_length=50, verbose_name='Qr Code')),
                ('qta', models.IntegerField(default=1, verbose_name='Q.tà')),
                ('rifacquisto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.aquistocard', verbose_name='Rif acquisto')),
            ],
            options={
                'verbose_name': "Lotto d'acquisto card",
                'verbose_name_plural': "Lotto d'acquisto card",
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/product')),
                ('descrizione', models.CharField(max_length=50, null=True, verbose_name='Descrizione')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data creazione')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('esperienza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.esperienze', verbose_name='Esperienza')),
                ('fornit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.fornitori', verbose_name='Fornitore')),
                ('sede', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portale.sedefornitori', verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.AddField(
            model_name='fornitori',
            name='tipologia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.tipologie', verbose_name='Tipo attività'),
        ),
        migrations.AddField(
            model_name='esperienze',
            name='fornit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.fornitori', verbose_name='Fornitore'),
        ),
        migrations.AddField(
            model_name='esperienze',
            name='sede',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portale.sedefornitori', verbose_name='Sede'),
        ),
        migrations.CreateModel(
            name='DocFornitore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.FileField(upload_to='%Y/%m/%d')),
                ('descrizione', models.CharField(max_length=50, null=True, verbose_name='Descrizione')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data creazione')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fornit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.fornitori', verbose_name='Fornitore')),
                ('sede', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='portale.sedefornitori', verbose_name='Sede')),
            ],
            options={
                'verbose_name': 'Documentazione Fornitore',
                'verbose_name_plural': 'Documentazione Fornitore',
            },
        ),
        migrations.CreateModel(
            name='Clienti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cognome', models.CharField(max_length=80, verbose_name='Cognome')),
                ('denominazione', models.CharField(blank=True, max_length=80, null=True, verbose_name='Ragione Sociale')),
                ('indirizzo', models.CharField(max_length=80, verbose_name='Indirizzo')),
                ('citta', models.CharField(max_length=50, verbose_name='Città')),
                ('pr', models.CharField(max_length=2, verbose_name='Provincia')),
                ('telefono', models.CharField(blank=True, max_length=16, null=True, verbose_name='Telefono')),
                ('cellulare', models.CharField(blank=True, max_length=16, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(blank=True, max_length=80, null=True, verbose_name='E-mail')),
                ('piva', models.CharField(blank=True, max_length=16, null=True, verbose_name='Partita iva')),
                ('codfisc', models.CharField(max_length=16, verbose_name='Codice fiscale')),
                ('numadulti', models.IntegerField(null=True, verbose_name='Numero Adulti nucleo familiare')),
                ('numabimbimax3', models.IntegerField(default=0, null=True, verbose_name='Numero Bambini nucleo familiare <= 3 anni')),
                ('numabimbimin3', models.IntegerField(default=0, null=True, verbose_name='Numero Bambini nucleo familiare > 3 anni')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data creazione')),
                ('qrcodecard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.lottiaquistocard', verbose_name='Qr Code')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Cienti',
            },
        ),
        migrations.AddField(
            model_name='aquistocard',
            name='TipoCard',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.tipocard', verbose_name='Tipologia card'),
        ),
        migrations.AddField(
            model_name='aquistocard',
            name='rivenditore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portale.rivenditori', verbose_name='Rivenditore'),
        ),
    ]
