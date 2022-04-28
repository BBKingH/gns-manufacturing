# Generated by Django 3.1.2 on 2022-04-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WfBendingStationList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Станції гнуття',
                'db_table': 'wf_bending_station_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfBendLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Логи гнуття',
                'db_table': 'wf_bend_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfConfigurationList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Конфігурації Топок',
                'db_table': 'wf_configuration_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfCutLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'wf_cut_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfDFXVersionControlLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Логи DFX Версій',
                'db_table': 'wf_dfx_version_control_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfFinalProductLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Логи фінального продукту',
                'db_table': 'wf_final_product_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfFireclayTypeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Типи шамотування',
                'db_table': 'wf_fireclay_type_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfFrameTypeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Типи рам',
                'db_table': 'wf_frame_type_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfGlassLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Логи скління',
                'db_table': 'wf_glass_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfGlazingTypeList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Типи скління',
                'db_table': 'wf_glazing_type_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfJobStatusList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Статуси виконання робіт',
                'db_table': 'wf_job_status_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfLocksmithLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Логи слюсарні',
                'db_table': 'wf_locksmith_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfModelList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Моделі Топок',
                'db_table': 'wf_model_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfOrderLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('delivery', models.TextField(blank=True, null=True)),
                ('mobile_number', models.TextField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('start_manufacturing', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(null=True)),
                ('deadline_date', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Логи Замовлень',
                'db_table': 'wf_order_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfPaymentList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Типи оплати',
                'db_table': 'wf_payment_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfPriorityList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Пріоритети',
                'db_table': 'wf_priority_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfQualityControlList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Контролі якості',
                'db_table': 'wf_quality_control_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfQualityControlLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Логи контролю якості',
                'db_table': 'wf_quality_control_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfStageFinalList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'wf_stage_final_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfStageList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'wf_stage_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfStageSemiFinishedList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'wf_stage_semi_finished_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfWeldingStationList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Станції зварювання',
                'db_table': 'wf_welding_station_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfWeldLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Логи зварювання',
                'db_table': 'wf_weld_log',
                'managed': False,
            },
        ),
    ]