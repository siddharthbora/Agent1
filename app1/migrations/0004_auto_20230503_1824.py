# Generated by Django 3.2.8 on 2023-05-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20230503_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='entry',
            name='brokerage_amount_buyer',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='brokerage_amount_seller',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='brokerage_buyer_clear_date',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='brokerage_seller_clear_date',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='interest',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='interest_d',
        ),
        migrations.AddField(
            model_name='entry',
            name='brokerage_amount_agent',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='brokerage_amount_agent2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='entry',
            name='lr_no',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='entry',
            name='transport_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='entry',
            name='viewer_name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='agent',
            name='outstanding_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='party',
            name='outstanding_balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='party',
            name='outstanding_brokerage',
            field=models.FloatField(default=0),
        ),
    ]
