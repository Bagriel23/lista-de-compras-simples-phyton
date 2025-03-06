class Item:
#   Estrutura um item da lista de compras.

    def __init__(self, id, name, unit, quantity, description):
#   Inicializa um item com ID, nome, unidade de medida, quantidade e descrição.

        self.id = id
        self.name = name
        self.unit = unit
        self.quantity = quantity
        self.description = description

    def __str__(self):
#   Retorna uma representação em string do item.

        return f"ID: {self.id} - {self.name} - {self.quantity} {self.unit} - {self.description}"

class ShoppingList:
#    Representa uma lista de compras com funcionalidades para adicionar, remover, pesquisar e listar itens.


    def __init__(self):
        self.items = []
        self.nextID = 1
        self.units = ['kg', 'g', 'l', 'ml', 'unidade(s)', 'm', 'cm']

    def add_item(self, name, unit, quantity, description):
#   Adiciona um novo item a lista de compras.

        item = Item(self.nextID, name, unit, quantity, description)
        self.items.append(item)
        self.nextID += 1
        print(f"'{name}' foi adicionado com sucesso!\n")

    def remove_item(self, id_item):
#   Remove um item já existente da lista de compras.

        removed_item = None
        for item in self.items:
            if item.id == id_item:
                self.items.remove(item)
                removed_item = item
                break
        if removed_item:
            print(f"'{removed_item.name}' foi removido com sucesso!\n")
        else:
            print("Produto não encontrado.\n")

    def search_item(self, search_term):
#   Pesquisa um item na lista de compras.

        found_item = [item for item in self.items if search_term.lower() in item.name.lower()]
        if found_item:
            print(f"\nProdutos encontrados: ({len(found_item)})")
            for item in found_item:
                print(item)
        else:
            print(f"\nNenhum produto '{search_term}' foi encontrado.\n")

    def list_items(self):
#   lista toda a lista de compras do usuário.

        if self.items:
            print(f"\nLista de produtos:\n")
            for item in self.items:
                print(item)
        else:
            print("\nNenhum produto na lista. Que tal adicionar alguns?\n")

def show_menu():
# Exibe o menu principal com todas as funções disponíveis.

    print("\n---- Menu ----")
    print("1 - Listar produtos")
    print("2 - Adicionar produto")
    print("3 - Remover produto")
    print("4 - Pesquisar produto")
    print("5 - Sair da lista")

def get_unit(units):
# Exibe opções de medida e permite a escolha de uma delas.

    print("\nEscolha uma medida: ")
    for i, unit in enumerate(shopping_list.units, 1):
        print(f"{i}. {unit}")
    while True:
        try:
            choose = int(input("\nInforme o número da unidade: "))
            if 1 <= choose <= len(shopping_list.units):
                return shopping_list.units[choose - 1]
            else:
                print("\nOpção inválida. Tente novamente.")
        except ValueError:
            print("\nEntrada inválida. Tente novamente.")

def main():
# Função principal que executa o loop de interação com o usuário.
5
    while True:
        show_menu()

        try:
            choose = int(input("O que deseja? "))
            if choose == 1:
                shopping_list.list_items()

            elif choose == 2:
                name = input("Por favor, informe o nome do produto: ")
                unit = get_unit(shopping_list.units)
                while True:
                    try:
                        quantity = float(input("Informe a quantidade: "))
                        break
                    except ValueError:
                        print("Quantidade inválida. Digite um número válido.")
                description = input("Por favor, informe o descricao do produto: ")
                shopping_list.add_item(name, unit, quantity, description)

            elif choose == 3:
                try:
                    id_item = int(input("Informe o ID do produto a ser removido: "))
                    shopping_list.remove_item(id_item)
                except ValueError:
                    print("ID inválido. Tente novamente com um ID válido.")
            elif choose == 4:
                search_term = input("Informe o nome do produto a ser pesquisado: ")
                shopping_list.search_item(search_term)

            elif choose == 5:
                print("Saindo do a lista! Boas compras e até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Tente um número válido.")

shopping_list = ShoppingList() #Criação de uma nova instância para a lista de compras.

main() #Chama a função principal, iniciando a execução do programa.