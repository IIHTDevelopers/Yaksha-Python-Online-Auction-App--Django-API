# Generated by Django 4.0 on 2022-05-31 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BidsModel',
            fields=[
                ('bid_id', models.AutoField(primary_key=True, serialize=False)),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bidding_date', models.DateField(auto_now_add=True)),
                ('product_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='productmodel',
            old_name='product_last_date_bidding',
            new_name='product_last_date_of_bidding',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='seller_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auctionapp.sellermodel'),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='customer_phone_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='product_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='seller_phone_number',
            field=models.IntegerField(),
        ),
    ]
