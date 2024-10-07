class Frutaria:
    def __init__(self):
        self.estoque = {}

    def adicionar_fruta(self, nome, quantidade, preco):
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
        else:
            self.estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print(f"Adicionadas {quantidade} unidades de {nome} ao estoque.")

    def ver_estoque(self):
        print("\nEstoque de Frutas:")
        for fruta, info in self.estoque.items():
            print(f"{fruta}: {info['quantidade']} unidades a R${info['preco']:.2f} cada")

    def vender_fruta(self, nome, quantidade):
        if nome in self.estoque and self.estoque[nome]['quantidade'] >= quantidade:
            total = quantidade * self.estoque[nome]['preco']
            self.estoque[nome]['quantidade'] -= quantidade
            print(f"Vendeu {quantidade} unidades de {nome}. Total: R${total:.2f}")
        else:
            print(f"Não há estoque suficiente de {nome}.")

def main():
    frutaria = Frutaria()

    while True:
        print("\nMenu:")
        print("1. Adicionar fruta")
        print("2. Ver estoque")
        print("3. Vender fruta")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome da fruta: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço por unidade: "))
            frutaria.adicionar_fruta(nome, quantidade, preco)
        
        elif escolha == '2':
            frutaria.ver_estoque()
        
        elif escolha == '3':
            nome = input("Nome da fruta a vender: ")
            quantidade = int(input("Quantidade: "))
            frutaria.vender_fruta(nome, quantidade)
        
        elif escolha == '4':
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

