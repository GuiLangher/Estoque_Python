# interface.py

import tkinter as tk
from tkinter import messagebox
from main import SistemaEstoque

class SistemaEstoqueGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sistema de Estoque")

        self.sistema_estoque = SistemaEstoque()

        self.label_nome = tk.Label(master, text="Nome do Produto")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1)

        self.label_quantidade = tk.Label(master, text="Quantidade")
        self.label_quantidade.grid(row=1, column=0)
        self.entry_quantidade = tk.Entry(master)
        self.entry_quantidade.grid(row=1, column=1)

        self.label_preco = tk.Label(master, text="Preço")
        self.label_preco.grid(row=2, column=0)
        self.entry_preco = tk.Entry(master)
        self.entry_preco.grid(row=2, column=1)

        self.label_id = tk.Label(master, text="ID do Produto")
        self.label_id.grid(row=3, column=0)
        self.entry_id = tk.Entry(master)
        self.entry_id.grid(row=3, column=1)

        self.button_adicionar = tk.Button(master, text="Adicionar Produto", command=self.adicionar_produto)
        self.button_adicionar.grid(row=4, column=0, columnspan=2)

        self.button_atualizar = tk.Button(master, text="Atualizar Produto", command=self.atualizar_produto)
        self.button_atualizar.grid(row=5, column=0, columnspan=2)

        self.button_deletar = tk.Button(master, text="Deletar Produto", command=self.deletar_produto)
        self.button_deletar.grid(row=6, column=0, columnspan=2)

        self.button_listar = tk.Button(master, text="Listar Produtos", command=self.listar_produtos)
        self.button_listar.grid(row=7, column=0, columnspan=2)

        self.text_output = tk.Text(master, height=10, width=50)
        self.text_output.grid(row=8, column=0, columnspan=2)

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        quantidade = int(self.entry_quantidade.get())
        preco = float(self.entry_preco.get())
        self.sistema_estoque.adicionar_produto(nome, quantidade, preco)
        messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado com sucesso!")

    def atualizar_produto(self):
        id = int(self.entry_id.get())
        nome = self.entry_nome.get()
        quantidade = int(self.entry_quantidade.get())
        preco = float(self.entry_preco.get())
        self.sistema_estoque.atualizar_produto(id, nome, quantidade, preco)
        messagebox.showinfo("Sucesso", f"Produto com ID {id} atualizado com sucesso!")

    def deletar_produto(self):
        id = int(self.entry_id.get())
        self.sistema_estoque.deletar_produto(id)
        messagebox.showinfo("Sucesso", f"Produto com ID {id} deletado com sucesso!")

    def listar_produtos(self):
        produtos = self.sistema_estoque.listar_produtos()
        self.text_output.delete(1.0, tk.END)
        if not produtos:
            self.text_output.insert(tk.END, "Estoque vazio.\n")
        else:
            for id, detalhes in produtos.items():
                self.text_output.insert(tk.END, f"ID: {id} | Nome: {detalhes['nome']} | Quantidade: {detalhes['quantidade']} | Preço: {detalhes['preco']}\n")

    def sair_programa():
        print()

if __name__ == "__main__":
    root = tk.Tk()
    sistema_estoque_gui = SistemaEstoqueGUI(root)
    root.mainloop()
