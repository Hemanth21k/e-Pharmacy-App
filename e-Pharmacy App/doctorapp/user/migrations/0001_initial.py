# Generated by Django 2.2.7 on 2020-07-20 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField()),
                ('ordered_items', models.ManyToManyField(to='cart.Cart')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default=True, max_length=50)),
                ('set_password', models.CharField(default=True, max_length=50)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'users'), (2, 'shops')], default=2)),
                ('shop_name', models.CharField(default=True, max_length=256)),
                ('shop_registration_no', models.CharField(default=True, max_length=256)),
                ('address', models.CharField(default=True, max_length=256)),
                ('latitude', models.FloatField(default=0, max_length=50)),
                ('longitude', models.FloatField(default=0, max_length=50)),
                ('distance', models.FloatField(default=0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'users'), (2, 'shops')], default=1)),
                ('signup_confirmation', models.BooleanField(default=False)),
                ('address', models.CharField(default=True, max_length=256)),
                ('cart_items', models.ManyToManyField(to='cart.Cart')),
                ('history', models.ManyToManyField(to='user.History')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]