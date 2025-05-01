from datetime import date
print(date.today().year)
ano = int(input('Ano de nascimento: '))
print(f'Quem nasceu em {ano} tem {date.today().year - ano} anos em {date.today().year}')
if date.today().year - ano < 18:
    print(f'Ainda falta {18 - (date.today().year - ano)} anos para o alistamento.')
    print(f'Seu alistamento sera em {ano + 18}')
if date.today().year - ano == 18:
    print('ja esta no ano do alistamento')
if date.today().year - ano > 18:
    print(f'Você já deveria ter se alistador há {date.today().year - (ano + 18)} anos para o alistamento.')
    print(f'Seu alistamento foi em {ano + 18}')
