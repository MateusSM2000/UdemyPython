from datetime import datetime
from dateutil.relativedelta import relativedelta

# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

parcela_por_ano = 1000000/5
parcela_por_mes = parcela_por_ano/12

data_inicial = datetime(2020, 12, 20)
time_delta = relativedelta(months=1)

qtd_parcelas = 5*12

print(f'Quantidade de parcelas: {qtd_parcelas}\n')

for parcela in range(1, 61):
    data_inicial += time_delta
    print(f'{parcela}x {datetime.strftime(data_inicial, '%d/%m/%Y')} R${parcela_por_mes:.2f}')