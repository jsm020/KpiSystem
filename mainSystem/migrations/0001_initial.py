# Generated by Django 5.0 on 2024-09-27 06:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('ilmiy_darajasi', models.CharField(blank=True, max_length=100, null=True)),
                ('kafedra', models.CharField(blank=True, max_length=100, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AKTDasturlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='akt_dasturlar_guvohnoma_files/', verbose_name="AKT dasturlari va elektron ma'lumotlar bazalari guvohnomalari")),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "AKT dasturlari va elektron ma'lumotlar bazalari uchun guvohnoma",
                'verbose_name_plural': "AKT dasturlari va elektron ma'lumotlar bazalari uchun guvohnomalar",
            },
        ),
        migrations.CreateModel(
            name='AxborotMurobbiylikSoat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Axborot va murobbiyslik soati',
                'verbose_name_plural': 'Axborot va murobbiyslik soatlari',
            },
        ),
        migrations.CreateModel(
            name='BirZiyoliBirMahalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='birziyoli_birmahalla_field/', verbose_name="Bir ziyoli – bir mahallaga ma'naviy homiy ishi")),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Bir ziyoli – bir mahallaga ma'naviy homiy",
                'verbose_name_plural': "Bir ziyoli – bir mahallaga ma'naviy homiy ishlari",
            },
        ),
        migrations.CreateModel(
            name='DarslikYokiQollanma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='darslik_yoki_qollanma_files/', verbose_name='Darslik yoki o‘quv qo‘llanma tayyorlash va nashr qilish')),
                ('link', models.URLField(verbose_name='Maqolaga havola')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Darslik yoki o‘quv qo‘llanma',
                'verbose_name_plural': 'Darsliklar yoki o‘quv qo‘llanmalar',
            },
        ),
        migrations.CreateModel(
            name='DarstanTashqariTadbirlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='darsdan_tashqari_files/', verbose_name="Darstdan tashqari madaniy va ma'rifiy tadbir")),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Darstdan tashqari tadbir',
                'verbose_name_plural': 'Darstdan tashqari tadbirlar',
            },
        ),
        migrations.CreateModel(
            name='DissertationHimoya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='dissertatsiya_himoya_files/', verbose_name='PhD yoki DSc dissertatsiyani himoya qilish')),
                ('link', models.URLField(verbose_name='Maqolaga havola')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dissertatsiyani himoya qilish',
                'verbose_name_plural': 'Dissertatsiyalar himoyalari',
            },
        ),
        migrations.CreateModel(
            name='FanVideoKontent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('link', models.URLField(verbose_name='Maqolaga havola')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fan video kontenti',
                'verbose_name_plural': 'Fan video kontentlari',
            },
        ),
        migrations.CreateModel(
            name='FaolInterfaolMetodlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Faol va interfaol metod',
                'verbose_name_plural': 'Faol va interfaol metodlar',
            },
        ),
        migrations.CreateModel(
            name='HIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='h_indeks_files/', verbose_name='Scopus, Web of Science va Google Scholar h-indeksiga egaligi')),
                ('link', models.URLField(verbose_name='H-indeks hujjatiga havola')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Scopus, Web of Science va Google Scholar h-indeksiga egaligi',
                'verbose_name_plural': 'Scopus, Web of Science va Google Scholar h-indeksiga egaligi',
            },
        ),
        migrations.CreateModel(
            name='HorijdaMalakaOshirish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='xorijda_malaka_oshirish_files/', verbose_name='Xorijda malaka oshirish yoki stajirovka')),
                ('link', models.URLField(verbose_name='Maqolaga havola')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Xorijda malaka oshirish',
                'verbose_name_plural': 'Xorijda malaka oshirishlar',
            },
        ),
        migrations.CreateModel(
            name='IlmiyRahbarlik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='ilmiy_rahbarlik_files/', verbose_name='Ilmiy rahbarlik')),
                ('link', models.URLField(verbose_name='Maqolaga havola')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ilmiy rahbarlik',
                'verbose_name_plural': 'Ilmiy rahbarliklar',
            },
        ),
        migrations.CreateModel(
            name='KonferensiyaMaqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='konferensiya_maqolalari_files/', verbose_name="Xalqaro va Respublika konferensiyalaridagi ma'ruza")),
                ('link', models.URLField(verbose_name="Ma'ruzaga havola")),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Xalqaro va Respublika konferensiyalarida ma'ruza",
                'verbose_name_plural': "Xalqaro va Respublika konferensiyalarida ma'ruza",
            },
        ),
        migrations.CreateModel(
            name='LoyihalarTayyorlash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='loyihalar_tayyorlash_files/', verbose_name='Loyiha tayyorlash')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Loyiha tayyorlash',
                'verbose_name_plural': 'Loyiha tayyorlash',
            },
        ),
        migrations.CreateModel(
            name='LoyihaMoliya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='loyiha_moliya_files/', verbose_name='Ilmiy loyihalarni moliyalashtirish')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ilmiy loyihalarni moliyalashtirish',
                'verbose_name_plural': 'Ilmiy loyihalarni moliyalashtirish',
            },
        ),
        migrations.CreateModel(
            name='MuhimTashabbuslarIshlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='muhim_tashabbus_field/', verbose_name='5 muhim tashabbus doirasidagi ishlari')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '5 muhim tashabbus ishi',
                'verbose_name_plural': '5 muhim tashabbus ishlari',
            },
        ),
        migrations.CreateModel(
            name='MustaqilTalimTopshiriqlari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "Mustaqil ta'lim topshiriqlari",
                'verbose_name_plural': "Mustaqil ta'lim topshiriqlari",
            },
        ),
        migrations.CreateModel(
            name='NashrEtilganDarsliklar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='nashr_etilgan_darsliklar_files/', verbose_name="Nashr etilgan darsliklar, qo'llanmalar va uslubiy ko'rsatmalar")),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Nashr etilgan darslik',
                'verbose_name_plural': 'Nashr etilgan darsliklar',
            },
        ),
        migrations.CreateModel(
            name='OAKJurnaliMaqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='oak_jurnal_maqolalar_files/', verbose_name='OAK tasarrufidagi jurnalda maqola chop etganligi')),
                ('link', models.URLField(verbose_name='Maqolaga havola')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OAK tasarrufidagi jurnalda maqola chop etganligi',
                'verbose_name_plural': 'OAK tasarrufidagi jurnalda maqola chop etganligi',
            },
        ),
        migrations.CreateModel(
            name='OqitishSifati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talim_sifat_xulosasi', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('talim_sifat', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('score', models.DecimalField(blank=True, decimal_places=1, editable=False, max_digits=2, null=True, verbose_name='Umumiy ball')),
                ('izoh', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "O'qitish sifati baholanishi",
                'verbose_name_plural': "O'qitish sifati baholanishi",
            },
        ),
        migrations.CreateModel(
            name='OquvYiliFanlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': "O'quv yili davomida fanlar bo'yicha resurslarni HEMIS tizimiga joylashtirish",
                'verbose_name_plural': "O'quv yili davomida fanlar bo'yicha resurslarni HEMIS tizimiga joylashtirish",
            },
        ),
        migrations.CreateModel(
            name='OtaOnalarIshlash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='ota_onalar_bilan_ishlash_field/', verbose_name='Talabalar ota-onalari bilan ishlash')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ota-onalar bilan ishlash',
                'verbose_name_plural': 'Ota-onalar bilan ishlash',
            },
        ),
        migrations.CreateModel(
            name='ScopusWebOfScience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='scopus_web_of_science_files/', verbose_name='Scopus va Web of Science xalqaro jurnallarida maqola chop etganligi')),
                ('link', models.URLField(verbose_name='Maqolaga havola')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Scopus va Web of Science xalqaro ilmiy-texnik bazasiga kiruvchi jurnalda maqola chop etganligi',
                'verbose_name_plural': 'Scopus va Web of Science xalqaro ilmiy-texnik bazasiga kiruvchi jurnalda maqola chop etganligi',
            },
        ),
        migrations.CreateModel(
            name='TalabaIlmiyFaoliyati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='talaba_ilmiy_faoliyati_files/', verbose_name='Talabaning ilmiy faoliyati')),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Talaba ilmiy faoliyati',
                'verbose_name_plural': 'Talaba ilmiy faoliyati',
            },
        ),
        migrations.CreateModel(
            name='TalabalarTurarJoyTadbirlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='talabalar_ttj_tadbirlar_files/', verbose_name="Talabalar turar joyidagi madaniy va ma'rifiy tadbir")),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Talabalar turar joyi tadbiri',
                'verbose_name_plural': 'Talabalar turar joyi tadbirlari',
            },
        ),
        migrations.CreateModel(
            name='TarbiyaTadbirlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maqola', models.FileField(upload_to='tarbiya_tadbirlar_files/', verbose_name="Talabalar bilan tarbiyaviy ish bo'yicha tadbir")),
                ('score', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Baholash')),
                ('izoh', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tarbiya tadbiri',
                'verbose_name_plural': 'Tarbiya tadbirlari',
            },
        ),
    ]
