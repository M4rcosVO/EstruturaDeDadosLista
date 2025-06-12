class Lista:
    def __init__(self):
        self.itens = []

    def pesquisar(self, item):
        if item not in self.itens:
            raise ValueError(f"Item '{item}' não encontrado na lista.")
        return self.itens.index(item)

    def retirar_pelo_valor(self, item):
        if item not in self.itens:
            raise ValueError(f"Item '{item}' não está presente na lista.")
        self.itens.remove(item)

    def esta_vazia(self):
        return len(self.itens) == 0

    def inserir_apos(self, i, item):
        if i < 0 or i >= len(self.itens):
            raise IndexError("Índice inválido. Não existe item na posição especificada.")
        self.itens.insert(i + 1, item)

    def retirar_por_indice(self, i):
        if i < 0 or i >= len(self.itens):
            raise IndexError("Índice inválido. Não existe item na posição especificada.")
        return self.itens.pop(i)

    def tamanho(self):
        return len(self.itens)

    def modificar_elemento(self, i, novo_valor):
        if i < 0 or i >= len(self.itens):
            raise IndexError("Índice inválido. Não existe item na posição especificada.")
        self.itens[i] = novo_valor

    def __str__(self):
        return str(self.itens)


# Exemplo de uso:
if __name__ == "__main__":
    lista = Lista()
    lista.itens = [10, 20, 30]
    print("Lista inicial:", lista)

    print("Índice do 20:", lista.pesquisar(20))

    lista.inserir_apos(1, 25)
    print("Após inserir 25 após o índice 1:", lista)

    lista.modificar_elemento(2, 26)
    print("Após modificar elemento na posição 2:", lista)

    lista.retirar_pelo_valor(10)
    print("Após remover o valor 10:", lista)

    lista.retirar_por_indice(0)
    print("Após retirar o item na posição 0:", lista)

    print("Lista está vazia?", lista.esta_vazia())
    print("Tamanho da lista:", lista.tamanho())
