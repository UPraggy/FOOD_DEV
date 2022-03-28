from traceback import print_list
import pandas as pd
pedido = pd.read_excel('0_PROJETOS_PORTIFOLIO/TESTE.xlsx')


entry = 'Roger' #input("ENTRY: ")
entry = pedido.loc[pedido['Client'] == str(entry)]


if (len(entry.index) > 1):
    print("Existe mais de um registo com o parametro passado \nSelecione o registro a ser atualizado: ")
    print(entry)
    entry = int(input("ENTRY: "))
else:
    entry = entry.index
# update_col = 'Client'
# update_data  ='Rafael'
update_col = input("Escolha o tipo do dado a ser atualizado: ")
update_data = input("Insira o novo dado: ")
new_df = pd.DataFrame({update_col : update_data}, index=[entry[0]])

pedido.update(new_df)

# print(entry)

# update_col = input("Escolha o tipo do dado a ser atualizado: ")
# update_data = input("Insira o novo dado: ")
# pedido = pedido.loc[entry.index]

#pedido = pedido.set_index('number_order')


print(pedido)

# for x in range(len(entry)):
#     pedido = pedido.drop([entry[x]])
# pedido = pedido.set_index('number_order')

# pedido.to_excel("0_PROJETOS_PORTIFOLIO/TESTE2.xlsx")