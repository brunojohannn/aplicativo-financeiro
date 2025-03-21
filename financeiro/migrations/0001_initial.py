# Generated by Django 5.1.7 on 2025-03-12 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.CharField(choices=[('receita', 'Receita'), ('despesa', 'Despesa')], max_length=7)),
                ('categoria', models.CharField(choices=[('credito', 'Credito'), ('debito', 'Debito'), ('pix', 'Pix'), ('boleto', 'Boleto'), ('dinheiro', 'Dinheiro')], max_length=10)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
