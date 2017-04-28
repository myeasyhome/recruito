# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 09:58
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('about', models.TextField(verbose_name='About')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('city', models.CharField(max_length=100, verbose_name='District')),
                ('state', models.CharField(max_length=100, verbose_name='State')),
                ('zipcode', models.CharField(max_length=100, verbose_name='Pincode / Zipcode')),
                ('phone_number', models.CharField(max_length=30, verbose_name='Phone Number')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rms.Company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Industry Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('last_date', models.DateField()),
                ('number_of_openings', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('keywords', models.CharField(blank=True, max_length=150)),
                ('job_location', models.CharField(blank=True, max_length=400)),
                ('min_year_of_experience', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('max_year_of_experience', models.DecimalField(decimal_places=1, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)])),
                ('min_salary', models.DecimalField(decimal_places=5, default=0, max_digits=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('max_salary', models.DecimalField(decimal_places=5, default=0, max_digits=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('salary_currency', models.CharField(choices=[('ALL', 'Albania Lek'), ('AFN', 'Afghanistan Afghani'), ('ARS', 'Argentina Peso'), ('AWG', 'Aruba Guilder'), ('AUD', 'Australia Dollar'), ('AZN', 'Azerbaijan New Manat'), ('BSD', 'Bahamas Dollar'), ('BBD', 'Barbados Dollar'), ('BDT', 'Bangladeshi taka'), ('BYR', 'Belarus Ruble'), ('BZD', 'Belize Dollar'), ('BMD', 'Bermuda Dollar'), ('BOB', 'Bolivia Boliviano'), ('BAM', 'Bosnia and Herzegovina Convertible Marka'), ('BWP', 'Botswana Pula'), ('BGN', 'Bulgaria Lev'), ('BRL', 'Brazil Real'), ('BND', 'Brunei Darussalam Dollar'), ('KHR', 'Cambodia Riel'), ('CAD', 'Canada Dollar'), ('KYD', 'Cayman Islands Dollar'), ('CLP', 'Chile Peso'), ('CNY', 'China Yuan Renminbi'), ('COP', 'Colombia Peso'), ('CRC', 'Costa Rica Colon'), ('HRK', 'Croatia Kuna'), ('CUP', 'Cuba Peso'), ('CZK', 'Czech Republic Koruna'), ('DKK', 'Denmark Krone'), ('DOP', 'Dominican Republic Peso'), ('XCD', 'East Caribbean Dollar'), ('EGP', 'Egypt Pound'), ('SVC', 'El Salvador Colon'), ('EEK', 'Estonia Kroon'), ('EUR', 'Euro Member Countries'), ('FKP', 'Falkland Islands (Malvinas) Pound'), ('FJD', 'Fiji Dollar'), ('GHC', 'Ghana Cedis'), ('GIP', 'Gibraltar Pound'), ('GTQ', 'Guatemala Quetzal'), ('GGP', 'Guernsey Pound'), ('GYD', 'Guyana Dollar'), ('HNL', 'Honduras Lempira'), ('HKD', 'Hong Kong Dollar'), ('HUF', 'Hungary Forint'), ('ISK', 'Iceland Krona'), ('INR', 'India Rupee'), ('IDR', 'Indonesia Rupiah'), ('IRR', 'Iran Rial'), ('IMP', 'Isle of Man Pound'), ('ILS', 'Israel Shekel'), ('JMD', 'Jamaica Dollar'), ('JPY', 'Japan Yen'), ('JEP', 'Jersey Pound'), ('KZT', 'Kazakhstan Tenge'), ('KPW', 'Korea (North) Won'), ('KRW', 'Korea (South) Won'), ('KGS', 'Kyrgyzstan Som'), ('LAK', 'Laos Kip'), ('LVL', 'Latvia Lat'), ('LBP', 'Lebanon Pound'), ('LRD', 'Liberia Dollar'), ('LTL', 'Lithuania Litas'), ('MKD', 'Macedonia Denar'), ('MYR', 'Malaysia Ringgit'), ('MUR', 'Mauritius Rupee'), ('MXN', 'Mexico Peso'), ('MNT', 'Mongolia Tughrik'), ('MZN', 'Mozambique Metical'), ('NAD', 'Namibia Dollar'), ('NPR', 'Nepal Rupee'), ('ANG', 'Netherlands Antilles Guilder'), ('NZD', 'New Zealand Dollar'), ('NIO', 'Nicaragua Cordoba'), ('NGN', 'Nigeria Naira'), ('NOK', 'Norway Krone'), ('OMR', 'Oman Rial'), ('PKR', 'Pakistan Rupee'), ('PAB', 'Panama Balboa'), ('PYG', 'Paraguay Guarani'), ('PEN', 'Peru Nuevo Sol'), ('PHP', 'Philippines Peso'), ('PLN', 'Poland Zloty'), ('QAR', 'Qatar Riyal'), ('RON', 'Romania New Leu'), ('RUB', 'Russia Ruble'), ('SHP', 'Saint Helena Pound'), ('SAR', 'Saudi Arabia Riyal'), ('RSD', 'Serbia Dinar'), ('SCR', 'Seychelles Rupee'), ('SGD', 'Singapore Dollar'), ('SBD', 'Solomon Islands Dollar'), ('SOS', 'Somalia Shilling'), ('ZAR', 'South Africa Rand'), ('LKR', 'Sri Lanka Rupee'), ('SEK', 'Sweden Krona'), ('CHF', 'Switzerland Franc'), ('SRD', 'Suriname Dollar'), ('SYP', 'Syria Pound'), ('TWD', 'Taiwan New Dollar'), ('THB', 'Thailand Baht'), ('TTD', 'Trinidad and Tobago Dollar'), ('TRY', 'Turkey Lira'), ('TRL', 'Turkey Lira'), ('TVD', 'Tuvalu Dollar'), ('UAH', 'Ukraine Hryvna'), ('GBP', 'United Kingdom Pound'), ('USD', 'United States Dollar'), ('UYU', 'Uruguay Peso'), ('UZS', 'Uzbekistan Som'), ('VEF', 'Venezuela Bolivar'), ('VND', 'Viet Nam Dong'), ('YER', 'Yemen Rial'), ('ZWD', 'Zimbabwe Dollar')], max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rms.Company')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rms.Designation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('recruiter', 'Recruiter'), ('candidate', 'Candidate')], max_length=25, verbose_name='Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ManyToManyField(to='rms.Skill'),
        ),
        migrations.AddField(
            model_name='company',
            name='industry_type',
            field=models.ManyToManyField(to='rms.IndustryType'),
        ),
    ]
