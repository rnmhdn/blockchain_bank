# Generated by Django 2.0 on 2018-07-13 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_auto_20180712_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='wallet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank_wallet', to='banking.Wallet'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='wallet',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='banking.Wallet'),
        ),
    ]