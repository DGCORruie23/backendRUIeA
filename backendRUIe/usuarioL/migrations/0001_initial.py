# Generated by Django 4.2.6 on 2023-11-13 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarioL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oficinaR', models.CharField(choices=[('AGUASCALIENTES', 'AGUASCALIENTES'), ('BAJA CALIFORNIA', 'BAJA CALIFORNIA'), ('BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA SUR'), ('CAMPECHE', 'CAMPECHE'), ('COAHUILA', 'COAHUILA'), ('COLIMA', 'COLIMA'), ('CHIAPAS', 'CHIAPAS'), ('CHIHUAHUA', 'CHIHUAHUA'), ('CDMX', 'CDMX'), ('DURANGO', 'DURANGO'), ('GUANAJUATO', 'GUANAJUATO'), ('GUERRERO', 'GUERRERO'), ('HIDALGO', 'HIDALGO'), ('JALISCO', 'JALISCO'), ('EDOMEX', 'EDOMEX'), ('MICHOACÁN', 'MICHOACÁN'), ('MORELOS', 'MORELOS'), ('NAYARIT', 'NAYARIT'), ('NUEVO LEÓN', 'NUEVO LEÓN'), ('OAXACA', 'OAXACA'), ('PUEBLA', 'PUEBLA'), ('QUERÉTARO', 'QUERÉTARO'), ('QUINTANA ROO', 'QUINTANA ROO'), ('SAN LUIS POTOSÍ', 'SAN LUIS POTOSÍ'), ('SINALOA', 'SINALOA'), ('SONORA', 'SONORA'), ('TABASCO', 'TABASCO'), ('TAMAULIPAS', 'TAMAULIPAS'), ('TLAXCALA', 'TLAXCALA'), ('VERACRUZ', 'VERACRUZ'), ('YUCATÁN', 'YUCATÁN'), ('ZACATECAS', 'ZACATECAS')], default='CDMX', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuarioL', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
