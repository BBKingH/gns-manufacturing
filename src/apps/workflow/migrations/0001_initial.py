# Generated by Django 4.0.4 on 2022-08-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Лог нотатки',
                'verbose_name_plural': 'Логи нотаток',
                'db_table': 'wf_note_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('delivery', models.TextField(blank=True, null=True)),
                ('mobile_number', models.TextField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('dxf_version', models.CharField(blank=True, max_length=100, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('start_manufacturing', models.BooleanField(default=False)),
                ('start_manufacturing_semi_finished', models.BooleanField(default=True)),
                ('is_canceled', models.BooleanField(default=False)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('deadline_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Лог Замовлень',
                'verbose_name_plural': 'Логи Замовлень',
                'db_table': 'wf_order_log',
                'ordering': ['-created_at'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfAuthUserGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Сферу працівників',
                'verbose_name_plural': 'Сфери працівників',
                'db_table': 'wf_auth_user_group',
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
                'verbose_name': 'Конфігурацію Топки',
                'verbose_name_plural': 'Конфігурації Топок',
                'db_table': 'wf_configuration_list',
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
                'verbose_name': 'Тип шамотування',
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
                'verbose_name': 'Тип рами',
                'verbose_name_plural': 'Типи рам',
                'db_table': 'wf_frame_type_list',
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
                'verbose_name': 'Тип скління',
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
                'verbose_name': 'Статус виконання робіт',
                'verbose_name_plural': 'Статуси виконання робіт',
                'db_table': 'wf_job_status_list',
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
                'verbose_name': 'Модель Топки',
                'verbose_name_plural': 'Моделі Топок',
                'db_table': 'wf_model_list',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfOrderWorkStage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_of_execution', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Стадія замовлення',
                'verbose_name_plural': 'Стадії замовлення',
                'db_table': 'wf_order_work_stage',
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
                'verbose_name': 'Тип олати',
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
                'verbose_name': 'Пріоритет',
                'verbose_name_plural': 'Пріоритети',
                'db_table': 'wf_priority_list',
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
            name='WfWorkLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Лог виробництва',
                'verbose_name_plural': 'Логи виробництва',
                'db_table': 'wf_work_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WfWorkStageList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Стадію виконання роботи',
                'verbose_name_plural': 'Стадії виконання роботи',
                'db_table': 'wf_work_stage_list',
                'managed': False,
            },
        ),
    ]
