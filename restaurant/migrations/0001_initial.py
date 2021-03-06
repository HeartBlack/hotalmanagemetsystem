# Generated by Django 4.0.5 on 2022-06-30 08:34

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


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
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_customer', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bar_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('price', models.FloatField(max_length=1000)),
                ('qty', models.FloatField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, null=True)),
                ('age', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('nationality', models.CharField(max_length=155)),
                ('country', models.CharField(max_length=255)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('user', models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('price', models.FloatField(max_length=1000)),
                ('qty', models.FloatField(max_length=255)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.category')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(default=True, max_length=255)),
                ('room_number', models.CharField(max_length=255)),
                ('room_type', models.CharField(max_length=255)),
                ('price_pernight', models.CharField(max_length=255)),
                ('max_person', models.IntegerField()),
                ('room_description', models.CharField(max_length=500)),
                ('booking_timeframe', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField(max_length=255, null=True)),
                ('total', models.CharField(max_length=255, null=True)),
                ('bar_items', models.ManyToManyField(to='restaurant.bar_items')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer')),
                ('kitchen_item', models.ManyToManyField(to='restaurant.kitchen_items')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, null=True)),
                ('age', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('nationality', models.CharField(max_length=155)),
                ('designation', models.CharField(max_length=255)),
                ('user', models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('av', 'available'), ('bk', 'booked')], max_length=255)),
                ('customer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.customer')),
                ('room_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.room')),
            ],
        ),
        migrations.AddField(
            model_name='bar_items',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.category'),
        ),
    ]
