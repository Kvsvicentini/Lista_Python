import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

class GerenciadorTarefas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Tarefas")

        self.lista = tk.Listbox(master, width=50)
        self.lista.pack(pady=10)

        self.botao_add = tk.Button(master, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_add.pack()

        self.botao_remover = tk.Button(master, text="Remover Tarefa", command=self.remover_tarefa)
        self.botao_remover.pack()

        self.conn = sqlite3.connect("tarefas.db")
        self.cursor = self.conn.cursor()
        self.criar_tabela()
        self.carregar_tarefas()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def adicionar_tarefa(self):
        tarefa = simpledialog.askstring("Adicionar Tarefa", "Digite a tarefa:")
        if tarefa:
            self.cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (tarefa,))
            self.conn.commit()
            self.carregar_tarefas()

    def remover_tarefa(self):
        selecionada = self.lista.curselection()
        if selecionada:
            tarefa = self.lista.get(selecionada)
            confirm = messagebox.askyesno("Remover", f"Remover a tarefa '{tarefa}'?")
            if confirm:
                self.cursor.execute("DELETE FROM tarefas WHERE descricao = ?", (tarefa,))
                self.conn.commit()
                self.carregar_tarefas()

    def carregar_tarefas(self):
        self.lista.delete(0, tk.END)
        self.cursor.execute("SELECT descricao FROM tarefas")
        for tarefa in self.cursor.fetchall():
            self.lista.insert(tk.END, tarefa[0])

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefas(root)
    root.mainloop()
