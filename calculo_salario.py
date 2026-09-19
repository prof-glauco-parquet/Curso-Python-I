from os import system
system('cls')

salario_bruto = float(input('Digite o seu salário bruto: R$').replace(',','.'))

# Cálcular INSS
if salario_bruto <= 1621.00:
    aliquota_inss = 0.075
    parcela_inss = 0
    inss = salario_bruto * aliquota_inss - parcela_inss
elif salario_bruto <= 2902.84:
    aliquota_inss = 0.09
    parcela_inss = 24.32
    inss = salario_bruto * aliquota_inss - parcela_inss
elif salario_bruto <= 4354.27:
    aliquota_inss = 0.12
    parcela_inss = 111.41
    inss = salario_bruto * aliquota_inss - parcela_inss
elif salario_bruto <= 8475.55:
    aliquota_inss = 0.14
    parcela_inss = 198.50
    inss = salario_bruto * aliquota_inss - parcela_inss
else:
    aliquota_inss = 0
    parcela_inss = 0
    inss = 988.07

print(f'Salário bruto: R${salario_bruto:.2f}')

print(f'Alíquota INSS: {aliquota_inss*100:.1f}%')
print(f'Parcela deduzida: R${parcela_inss:.2f}')
print(f'Valor do INSS: R${inss:.2f}')

salario_inss = salario_bruto - inss

# Calcular IRPF
if salario_inss <= 2428.80:
    aliquota_irpf = 0
    parcela_irpf = 0
elif salario_inss <= 2826.65:
    aliquota_irpf = 0.075
    parcela_irpf = 182.16
elif salario_inss <= 3751.05:
    aliquota_irpf = 0.15
    parcela_irpf = 394.16
elif salario_inss <= 4664.68:
    aliquota_irpf = 0.225
    parcela_irpf = 675.49
else:
    aliquota_irpf = 0.275
    parcela_irpf = 908.73

irpf = salario_inss * aliquota_irpf - parcela_irpf

print(f'Salário base IRPF: R${salario_inss:.2f}')
print(f'Alíquota IRPF: {aliquota_irpf*100:.1f}%')
print(f'Parcela deduzida: R${parcela_irpf:.2f}')
print(f'Valor do IRPF: R${irpf:.2f}')

salario_liquido = salario_bruto - inss - irpf
print(f'Salário líquido: R$ {salario_liquido:.2f}')