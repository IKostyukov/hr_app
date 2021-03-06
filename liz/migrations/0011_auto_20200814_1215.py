# Generated by Django 3.0.7 on 2020-08-14 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('liz', '0010_auto_20200630_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'вариант для ответа', 'verbose_name_plural': '№6: варианты для ответов'},
        ),
        migrations.AlterModelOptions(
            name='appointto',
            options={'verbose_name': ' опросник  сотруднику ', 'verbose_name_plural': '№4: назначить опросник'},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'сотрудник', 'verbose_name_plural': '№1: сотрудники'},
        ),
        migrations.AlterModelOptions(
            name='employeeanswer',
            options={'verbose_name': 'ответы сотрудников', 'verbose_name_plural': '№5: посмотреть ответы сотрудников'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'вопрос', 'verbose_name_plural': '№2: вопросы'},
        ),
        migrations.AlterModelOptions(
            name='questionnaire',
            options={'verbose_name': 'опросник', 'verbose_name_plural': '№3: сформировать опросник'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_all_variants',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_right',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answer_weight',
        ),
        migrations.AddField(
            model_name='answer',
            name='time_for_answer',
            field=models.PositiveSmallIntegerField(default=15, verbose_name='время на ответ, сек.'),
        ),
        migrations.AddField(
            model_name='employeeanswer',
            name='in_time',
            field=models.BooleanField(default=True, verbose_name='вовремя'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_right_variant',
            field=models.BooleanField(verbose_name='укажите правильный ли это вариант?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='liz.Question', verbose_name='вопросы'),
        ),
        migrations.AlterField(
            model_name='appointto',
            name='questionnaires',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='appoint', to='liz.Questionnaire', verbose_name='опросник'),
        ),
        migrations.AlterField(
            model_name='employeeanswer',
            name='is_correct',
            field=models.BooleanField(default=False, verbose_name='верно'),
        ),
        migrations.AlterField(
            model_name='employeeanswer',
            name='questionnaires',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_questionnaire', to='liz.Questionnaire', verbose_name='опросник'),
        ),
        migrations.AlterField(
            model_name='employeeanswer',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_question', to='liz.Question', verbose_name='вопрос'),
        ),
        migrations.AlterField(
            model_name='employeeanswer',
            name='user_answer',
            field=models.CharField(max_length=256, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='employeeanswer',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='liz.Employee', verbose_name='сотрудники'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='user', through='liz.AppointTo', to='liz.Employee', verbose_name='Открытые для отрудников'),
        ),
    ]
