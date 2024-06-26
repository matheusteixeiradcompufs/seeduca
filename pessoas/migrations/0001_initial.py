# Generated by Django 4.2.7 on 2024-04-27 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import escolas.models.base_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escolas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaRecados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'agenda de recados',
                'verbose_name_plural': 'agendas de recados',
            },
        ),
        migrations.CreateModel(
            name='Boletim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('A', 'Aprovado'), ('M', 'Matriculado'), ('T', 'Transferido'), ('RM', 'Reprovado por média'), ('RF', 'Reprovado por falta'), ('RFM', 'Reprovado por falta e por média')], default='M', max_length=30)),
                ('encerrar', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='boletins_qr_codes/')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turma_boletins', to='escolas.turma')),
            ],
            options={
                'verbose_name_plural': 'boletins',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=10, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('uid', models.CharField(blank=True, max_length=100, null=True)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_pessoa', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('ano', escolas.models.base_model.YearField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100)])),
                ('tipo', models.CharField(choices=[('C', 'CARRO'), ('O', 'ÔNIBUS'), ('V', 'VAN'), ('X', 'OUTROS')], max_length=20, verbose_name='tipo do veículo')),
                ('nomeMotorista', models.CharField(blank=True, max_length=100, null=True, verbose_name='nome do motorista')),
                ('nomeAuxiliar', models.CharField(blank=True, max_length=100, null=True, verbose_name='nome do auxiliar')),
                ('itinerario', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoas.pessoa')),
                ('eh_pcd', models.BooleanField(default=False)),
                ('descricao_pcd', models.TextField(blank=True, null=True, verbose_name='descrição da pcd')),
                ('retrato', models.ImageField(blank=True, default='', null=True, upload_to='alunos_retratos/')),
            ],
            bases=('pessoas.pessoa',),
        ),
        migrations.CreateModel(
            name='TelefoneTransporte',
            fields=[
                ('telefone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escolas.telefone')),
                ('transporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transporte_telefones', to='pessoas.transporte')),
            ],
            options={
                'verbose_name': 'telefone',
            },
            bases=('escolas.telefone',),
        ),
        migrations.CreateModel(
            name='TelefonePessoa',
            fields=[
                ('telefone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escolas.telefone')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_telefones', to='pessoas.pessoa')),
            ],
            options={
                'verbose_name': 'telefone',
            },
            bases=('escolas.telefone',),
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(blank=True, choices=[('A', 'Aprovado'), ('R', 'Reprovado')], max_length=10, null=True)),
                ('finalizar', models.BooleanField(default=False)),
                ('boletim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletim_situacoes', to='pessoas.boletim')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_situacoes', to='escolas.disciplina')),
            ],
            options={
                'verbose_name': 'situação',
                'verbose_name_plural': 'situações',
            },
        ),
        migrations.CreateModel(
            name='Recado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('eh_aluno', models.BooleanField(default=False)),
                ('publicado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda_recados', to='pessoas.agendarecados')),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_recados', to='pessoas.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentual', models.FloatField(default=0)),
                ('boletim', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='boletim_frequencia', to='pessoas.boletim')),
            ],
            options={
                'verbose_name': 'frequência',
            },
        ),
        migrations.CreateModel(
            name='EmailPessoa',
            fields=[
                ('email_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escolas.email')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa_emails', to='pessoas.pessoa')),
            ],
            options={
                'verbose_name': 'e-mail',
            },
            bases=('escolas.email',),
        ),
        migrations.AddField(
            model_name='agendarecados',
            name='boletim',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='boletim_agendas', to='pessoas.boletim'),
        ),
        migrations.AddField(
            model_name='transporte',
            name='alunos',
            field=models.ManyToManyField(blank=True, related_name='alunos_transportes', to='pessoas.aluno'),
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('observacao', models.TextField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluno_responsaveis', to='pessoas.aluno')),
            ],
            options={
                'verbose_name': 'responsável',
                'verbose_name_plural': 'responsáveis',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('M1', 'Média 1'), ('M2', 'Média 2'), ('MG', 'Média Geral')], max_length=100)),
                ('valor', models.FloatField(default=0)),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizada_em', models.DateTimeField(auto_now=True)),
                ('boletim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletim_medias', to='pessoas.boletim')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_medias', to='escolas.disciplina')),
            ],
            options={
                'verbose_name': 'média',
                'verbose_name_plural': 'médias',
                'unique_together': {('tipo', 'disciplina', 'boletim')},
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pessoas.pessoa')),
                ('formacao', models.TextField(blank=True, null=True)),
                ('retrato', models.ImageField(blank=True, default='', null=True, upload_to='funcionarios_retratos/')),
                ('turmas', models.ManyToManyField(blank=True, related_name='turmas_funcionarios', to='escolas.turma')),
            ],
            options={
                'verbose_name': 'funcionário',
                'verbose_name_plural': 'funcionários',
            },
            bases=('pessoas.pessoa',),
        ),
        migrations.CreateModel(
            name='DiaLetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('presenca', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('frequencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frequencia_diasletivos', to='pessoas.frequencia')),
            ],
            options={
                'verbose_name': 'dia letivo',
                'verbose_name_plural': 'dias letivos',
                'unique_together': {('data', 'frequencia')},
            },
        ),
        migrations.AddField(
            model_name='boletim',
            name='aluno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluno_boletins', to='pessoas.aluno'),
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('A1', '1ª Avaliação'), ('A2', '2ª Avaliação'), ('R1', '1ª Recuperação'), ('A3', '3ª Avaliação'), ('A4', '4ª Avaliação'), ('R2', '2ª Recuperação')], max_length=100)),
                ('nota', models.FloatField(default=0)),
                ('confirmar', models.BooleanField(default=False)),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizada_em', models.DateTimeField(auto_now=True)),
                ('boletim', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boletim_avaliacoes', to='pessoas.boletim')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplina_avaliacoes', to='escolas.disciplina')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aluno_avaliacoes', to='pessoas.aluno')),
            ],
            options={
                'verbose_name': 'avaliação',
                'verbose_name_plural': 'avaliações',
            },
        ),
        migrations.AlterUniqueTogether(
            name='transporte',
            unique_together={('placa', 'ano')},
        ),
        migrations.AlterUniqueTogether(
            name='boletim',
            unique_together={('aluno', 'turma')},
        ),
    ]
