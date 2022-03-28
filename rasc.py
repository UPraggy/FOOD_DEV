pedido = pd.read_excel('0_PROJETOS_PORTIFOLIO/TESTE.xlsx')

print("Insira o conjunto de dados:")
cols = ["number_order", "client", "address", "status", "products", "delivery_fee", "value", "payment_form", "card_number"]

print(list(pedido.columns))
#dados = [x for x in range(9)]

# for x in range(9):
#     dados[x] = input(f'insira o {cols[x]}:')

# dados = [tuple(dados)]

dados = [ (202201, "Moni", "moon house", "delivering", "coca cola", "Gered", 500, "money", " ")]
New_df = pd.DataFrame(dados, columns = cols)
pedido = pedido.append(New_df,ignore_index=True)
pedido = pedido.set_index('number_order')
pedido.to_excel("0_PROJETOS_PORTIFOLIO/TESTE.xlsx")


# new_data_list2 = [ (202201, "Moni", "moon house", "delivering", "coca cola", "Gered", 500, "money", " ")]
# New_df = pd.DataFrame(new_data_list2, columns = ["number_order", "client", "address", "status", "products", 
# "delivery_fee", "value", "payment_form", "card_number"])
# pedido = pedido.append(New_df,ignore_index=True)


#print(pedido)

def delete_data(file_path_origin, file_path_destination ):
    data = pd.read_excel(f'{file_path_origin}')
    cols = data.columns
    input_data = input("ENTRY: ")
    input_data = data.loc[data[cols[0]] == int(input_data)]
    input_data = input_data.index
    if(len(input_data) == 0):
        print("Entrada Invalida")
    else:
        for x in range(len(input_data)):
                data = data.drop([input_data[x]])
    data = data.set_index(f'{cols[0]}')
    data.to_excel(f'{file_path_destination}')

entry = input("ENTRY: ")
entry = pedido.loc[pedido['number_order'] == int(entry)]

if (len(entry.index) > 1):
    print("Existe mais de um registo com o parametro passado \nSelecione o registro a ser apagado: ")
    print(entry)
    registro = int(input("ENTRY: "))
    pedido = pedido.drop([registro])
else:
    entry = entry.index
    pedido = pedido.drop([entry[0]])

pedido = pedido.set_index('number_order')


print(pedido)
