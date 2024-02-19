# Generated by Django 5.0.2 on 2024-02-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0004_customer_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PIC',
            fields=[
                ('PIC_Id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nama', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telp', models.PositiveIntegerField()),
                ('Role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_pt', models.CharField(max_length=255)),
                ('alamat_penagihan', models.CharField(max_length=255)),
                ('alamat_pengiriman', models.CharField(max_length=255)),
                ('telp', models.PositiveIntegerField()),
                ('terms_of_payment', models.CharField(max_length=10)),
                ('pengiriman', models.CharField(max_length=50)),
                ('npwp', models.CharField(max_length=255)),
                ('faktur', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='pengiriman',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='telp',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='terms_of_payment',
            field=models.CharField(max_length=10),
        ),
    ]
