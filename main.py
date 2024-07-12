class SistemaEstoque:
    def __init__(self):
        self.estoque = {}
        self.id_atual = 1


    def adicionar_produto(self, nome, quantidade, preco):
        self.estoque[self.id_atual] = {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }
        self.id_atual += 1
        print(f"Produto {nome} adicionado com sucesso")


    def listar_produtos(self):
        if not self.estoque:
            print("Estoque vazio")
        else:
            for id, detalhes in self. estoque.items():
                print(f"ID: {id} | Nome: {detalhes['nome']} | Quantidade: {detalhes['quantidade']} | Preço: {detalhes['preco']}")


    def atualizar_produto(self, id, nome=None, quantidade=None, preco=None):
        if id in self.estoque:
            if nome:
                self.estoque[id]['nome'] = nome
            if quantidade is not None:
                self.estoque[id]['quantidade'] = quantidade
            if preco is not None:
                self.estoque[id]['preco'] = preco
            print(f"Produto com ID {id} atulizado com sucesso")
        else:
            print("Produto não encontrado.")

    def deletar_produto(self,id):
        if id in self.estoque:
            del self.estoque[id]
            print(f"Produto com ID {id} deletado com sucesso")
        else:
            print("Estoque não encontrado")

