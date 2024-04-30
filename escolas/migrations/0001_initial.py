# Generated by Django 4.2.7 on 2024-04-27 12:49

from django.db import migrations, models
import django.db.models.deletion
import escolas.models.base_model


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaEscolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'agenda escolar',
                'verbose_name_plural': 'agendas escolares',
            },
        ),
        migrations.CreateModel(
            name='AvisoBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('publicado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DiaAgenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('util', models.BooleanField(default=False)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda_dias', to='escolas.agendaescolar')),
            ],
            options={
                'verbose_name': 'dia da agenda',
                'verbose_name_plural': 'dias da agenda',
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('num_salas', models.IntegerField(default=0)),
                ('quantidade_alunos', models.IntegerField(default=0)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('imagem', models.ImageField(blank=True, default='', null=True, upload_to='escolas_images/')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCardapioMerenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ítem do cardápio',
                'verbose_name_plural': 'ítens do cardápio',
            },
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('quantidade_alunos', models.IntegerField(default=0)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='escola_salas', to='escolas.escola')),
            ],
            options={
                'unique_together': {('numero', 'escola')},
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('ano', escolas.models.base_model.YearField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100)])),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=10)),
                ('criada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizada_em', models.DateTimeField(auto_now=True)),
                ('disciplinas', models.ManyToManyField(blank=True, related_name='disciplinas_turmas', to='escolas.disciplina')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sala_turmas', to='escolas.sala')),
            ],
            options={
                'unique_together': {('nome', 'ano', 'turno', 'sala')},
            },
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('tipo', models.CharField(choices=[('E', 'Escola'), ('C', 'Casa')], max_length=10)),
                ('cadastrada_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('entrega', models.DateTimeField(blank=True, null=True)),
                ('diaAgenda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dia_tarefas', to='escolas.diaagenda', verbose_name='dia da agenda')),
            ],
        ),
        migrations.AddField(
            model_name='diaagenda',
            name='disciplinas',
            field=models.ManyToManyField(blank=True, related_name='disciplinas_dias', to='escolas.disciplina'),
        ),
        migrations.AddField(
            model_name='agendaescolar',
            name='turma',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='turma_agenda', to='escolas.turma'),
        ),
        migrations.CreateModel(
            name='TelefoneEscola',
            fields=[
                ('telefone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escolas.telefone')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escola_telefones', to='escolas.escola')),
            ],
            options={
                'verbose_name': 'telefone',
            },
            bases=('escolas.telefone',),
        ),
        migrations.CreateModel(
            name='MuralAvisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', escolas.models.base_model.YearField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027), (2028, 2028), (2029, 2029), (2030, 2030), (2031, 2031), (2032, 2032), (2033, 2033), (2034, 2034), (2035, 2035), (2036, 2036), (2037, 2037), (2038, 2038), (2039, 2039), (2040, 2040), (2041, 2041), (2042, 2042), (2043, 2043), (2044, 2044), (2045, 2045), (2046, 2046), (2047, 2047), (2048, 2048), (2049, 2049), (2050, 2050), (2051, 2051), (2052, 2052), (2053, 2053), (2054, 2054), (2055, 2055), (2056, 2056), (2057, 2057), (2058, 2058), (2059, 2059), (2060, 2060), (2061, 2061), (2062, 2062), (2063, 2063), (2064, 2064), (2065, 2065), (2066, 2066), (2067, 2067), (2068, 2068), (2069, 2069), (2070, 2070), (2071, 2071), (2072, 2072), (2073, 2073), (2074, 2074), (2075, 2075), (2076, 2076), (2077, 2077), (2078, 2078), (2079, 2079), (2080, 2080), (2081, 2081), (2082, 2082), (2083, 2083), (2084, 2084), (2085, 2085), (2086, 2086), (2087, 2087), (2088, 2088), (2089, 2089), (2090, 2090), (2091, 2091), (2092, 2092), (2093, 2093), (2094, 2094), (2095, 2095), (2096, 2096), (2097, 2097), (2098, 2098), (2099, 2099), (2100, 2100)])),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escola_murais', to='escolas.escola')),
            ],
            options={
                'verbose_name': 'mural de avisos',
                'verbose_name_plural': 'Murais de avisos',
                'unique_together': {('ano', 'escola')},
            },
        ),
        migrations.CreateModel(
            name='EmailEscola',
            fields=[
                ('email_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escolas.email')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escola_emails', to='escolas.escola')),
            ],
            options={
                'verbose_name': 'e-mail',
            },
            bases=('escolas.email',),
        ),
        migrations.AlterUniqueTogether(
            name='diaagenda',
            unique_together={('data', 'agenda')},
        ),
        migrations.CreateModel(
            name='CardapioMerenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=50)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escola_cardapios', to='escolas.escola')),
                ('itens', models.ManyToManyField(blank=True, related_name='cardapios_itens', to='escolas.itemcardapiomerenda')),
            ],
            options={
                'verbose_name': 'cardápio da merenda',
                'verbose_name_plural': 'cardápios da merenda',
                'unique_together': {('data', 'turno')},
            },
        ),
        migrations.CreateModel(
            name='AvisoEscola',
            fields=[
                ('avisobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escolas.avisobase')),
                ('mural', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mural_avisos', to='escolas.muralavisos', verbose_name='mural de avisos')),
            ],
            options={
                'verbose_name': 'aviso da escola',
                'verbose_name_plural': 'Avisos da escola',
            },
            bases=('escolas.avisobase',),
        ),
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('avisobase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='escolas.avisobase')),
                ('diaAgenda', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dia_avisos', to='escolas.diaagenda', verbose_name='dia da agenda')),
            ],
            bases=('escolas.avisobase',),
        ),
    ]
