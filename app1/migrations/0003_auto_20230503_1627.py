# Generated by Django 3.2.8 on 2023-05-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20230503_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='remaining_balance',
        ),
        migrations.RemoveField(
            model_name='party',
            name='remaining_balance',
        ),
        migrations.AddField(
            model_name='agent',
            name='outstanding_balance',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='party',
            name='outstanding_balance',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agent',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='amount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='brokerage_amount_buyer',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='brokerage_amount_seller',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='clear_date',
            field=models.CharField(default='[]', max_length=1500),
        ),
        migrations.AlterField(
            model_name='entry',
            name='interest',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rate',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='party',
            name='outstanding_brokerage',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='party',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
    ]
