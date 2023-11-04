import csv

def convert_to_mobills_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        data = list(reader)

    mobills_data = []
    rejected_data = []
    
    for i, row in enumerate(data):
        if i == 0:
            new_row = ["Data", "Descrição", "Valor", "Conta", "Categoria"]
            rejected_data.append(new_row)
            mobills_data.append(new_row)
            continue
        
        date = row[0]
        description = row[4]
        value = float(row[8]) * -1
        account = account_name
        category = rework_category(row[3], description)
        new_row = [date, description, value, account, category]

        if value > 0:
            rejected_data.append(new_row)
        else:
            mobills_data.append(new_row)
        
    with open(output_file, 'w', newline='', encoding='utf-16') as csv_file:
        writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerows(mobills_data)

    with open(rejected_file, 'w', newline='', encoding='utf-16') as csv_file:
        writer = csv.writer(csv_file, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerows(rejected_data)



# Categories to be used in Mobills:
# Alimentação
# Doação
# Entretenimento
# Pets
# Saúde
# Serviços
# Transporte
# Varejo
def rework_category(category, description):
    reworked_category = category
    
    if category == "Assistência médica e odontológica":
        reworked_category = "Saúde"

    elif "IFOOD" in description:
        reworked_category = "Alimentação"

    elif "GOOGLE YOUTUB" in description:
        reworked_category = "Entretenimento"

    elif "AMAZON" in description \
      or "MERCADOLIVRE" in description:
        reworked_category = "Varejo"
    
    elif "UBER" in description:
        reworked_category = "Transporte"

    elif "PET LOV" in description \
      or "PETLOV" in description \
      or "PETZ" in description:
        reworked_category = "Pets"

    elif "APOIASE" in description \
      or "PADRIM" in description:
        reworked_category = "Doação"

    elif category == "Relacionados a Automotivo":
        reworked_category = "Transporte"

    elif category == "TV por assinatura / Serviços de rádio":
        reworked_category = "Entretenimento"

    elif category == "Supermercados / Mercearia / Padarias / Lojas de Conveniência" \
      or category == "Restaurante / Lanchonete / Bar":
        reworked_category = "Alimentação"

    elif category == "Serviços Profissionais" \
      or category == "Serviços pessoais" \
      or category == "Consertos em Geral" \
      or category == "Serviços de telecomunicações":
        reworked_category = "Serviços"

    elif category == "Especialidade varejo" \
      or category == "Departamento / Desconto" \
      or category == "Casa / Escritório Mobiliário" \
      or category == "Vestuário / Roupas" \
      or category == "Empresa para empresa" \
      or category == "Marketing Direto":
        reworked_category = "Varejo"

    return reworked_category



# Uso
input_file = 'input.csv'  # Input CSV with data from C6 Bank
output_file = 'output.csv'  # Output CSV to be imported into Mobills
rejected_file = 'rejected.csv'  # Transactions that cannot be imported into Mobills
account_name = 'C6'  #Replace by account name or credit card in Mobills app



convert_to_mobills_csv(input_file, output_file)
