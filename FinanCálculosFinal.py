#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk
from tkinter import messagebox

class FinanceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("FinanCálculos   (By: Matheus Amaral da Rocha)")
        self.root.geometry("500x600")
        self.create_widgets()

    def create_widgets(self):
        self.titulo = tk.Label(self.root, text="------ FinanCálculos ------\nBy : ( Matheus Amaral da Rocha )", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=10)

        self.tipo_calculo = tk.StringVar(value="Imposto")
        self.opcoes_calculo = ["Imposto", "Desconto", "Juros", "Lucro e Margem", "Comissão"]
        self.menu_calculo = tk.OptionMenu(self.root, self.tipo_calculo, *self.opcoes_calculo, command=self.atualizar_interface)
        self.menu_calculo.pack(pady=10)

        self.frame_calculo = tk.Frame(self.root)
        self.frame_calculo.pack(fill="both", expand=True, padx=10, pady=10)

        self.atualizar_interface()

    def atualizar_interface(self, *args):
        for widget in self.frame_calculo.winfo_children():
            widget.destroy()

        tipo = self.tipo_calculo.get()
        if tipo == "Imposto":
            self.create_imposto_tab()
        elif tipo == "Desconto":
            self.create_desconto_tab()
        elif tipo == "Juros":
            self.create_juros_tab()
        elif tipo == "Lucro e Margem":
            self.create_lucro_margem_tab()
        elif tipo == "Comissão":
            self.create_comissao_tab()

    def create_imposto_tab(self):
        self.entry_valor = self.create_entry_field("Valor do Produto/Serviço:", 0)
        self.entry_taxa = self.create_entry_field("Taxa de Imposto (%):", 1)
        self.resultado_imposto = self.create_result_label(2)
        self.create_calculate_button(self.calcular_imposto, 3)

    def create_desconto_tab(self):
        self.entry_valor_desconto = self.create_entry_field("Valor do Produto/Serviço:", 0)
        self.desconto_tipo = tk.StringVar(value="percentual")
        self.create_radio_buttons("Tipo de Desconto:", ["percentual", "fixo"], self.desconto_tipo, 1)
        self.entry_desconto = self.create_entry_field("Valor do Desconto:", 2)
        self.resultado_desconto = self.create_result_label(3)
        self.create_calculate_button(self.calcular_desconto, 4)

    def create_juros_tab(self):
        self.entry_capital = self.create_entry_field("Capital Inicial (R$):", 0)
        self.entry_taxa_juros = self.create_entry_field("Taxa de Juros (%):", 1)
        self.entry_tempo = self.create_entry_field("Período (Anos):", 2)
        self.juros_tipo = tk.StringVar(value="simples")
        self.create_radio_buttons("Tipo de Juros:", ["simples", "composto"], self.juros_tipo, 3)
        self.resultado_juros = self.create_result_label(4)
        self.create_calculate_button(self.calcular_juros, 5)

    def create_lucro_margem_tab(self):
        self.entry_receita = self.create_entry_field("Receita Total (R$):", 0)
        self.entry_custo = self.create_entry_field("Custo Total (R$):", 1)
        self.resultado_lucro = self.create_result_label(2)
        self.create_calculate_button(self.calcular_lucro_margem, 3)

    def create_comissao_tab(self):
        self.entry_venda = self.create_entry_field("Valor da Venda (R$):", 0)
        self.entry_comissao = self.create_entry_field("Taxa de Comissão (%):", 1)
        self.resultado_comissao = self.create_result_label(2)
        self.create_calculate_button(self.calcular_comissao, 3)

    def create_entry_field(self, label_text, row):
        tk.Label(self.frame_calculo, text=label_text).grid(row=row, column=0, padx=10, pady=5)
        entry = tk.Entry(self.frame_calculo)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    def create_radio_buttons(self, label_text, options, variable, row):
        tk.Label(self.frame_calculo, text=label_text).grid(row=row, column=0, padx=10, pady=5)
        for i, option in enumerate(options):
            tk.Radiobutton(self.frame_calculo, text=option, variable=variable, value=option).grid(row=row, column=1+i, padx=10, pady=5)

    def create_result_label(self, row):
        resultado = tk.Label(self.frame_calculo, text="", font=("Arial", 12))
        resultado.grid(row=row, column=0, columnspan=2)
        return resultado

    def create_calculate_button(self, command, row):
        tk.Button(self.frame_calculo, text="Calcular", command=command).grid(row=row, column=0, columnspan=2, pady=10)

    def calcular_imposto(self):
        try:
            valor = float(self.entry_valor.get())
            taxa_imposto = float(self.entry_taxa.get())
            imposto = valor * (taxa_imposto / 100)
            self.resultado_imposto.config(text=f"Imposto: R${imposto:.2f}\nTotal: R${valor + imposto:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")

    def calcular_desconto(self):
        try:
            valor = float(self.entry_valor_desconto.get())
            if self.desconto_tipo.get() == 'percentual':
                desconto = float(self.entry_desconto.get())
                valor_desconto = valor * (desconto / 100)
            else:
                valor_desconto = float(self.entry_desconto.get())
            self.resultado_desconto.config(text=f"Desconto: R${valor_desconto:.2f}\nFinal: R${valor - valor_desconto:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")

    def calcular_juros(self):
        try:
            capital = float(self.entry_capital.get())
            taxa = float(self.entry_taxa_juros.get())
            tempo = int(self.entry_tempo.get())
            if self.juros_tipo.get() == 'simples':
                juros = capital * (taxa / 100) * tempo
            else:
                juros = capital * (1 + (taxa / 100)) ** tempo - capital
            self.resultado_juros.config(text=f"Juros: R${juros:.2f}\nTotal: R${capital + juros:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")

    def calcular_lucro_margem(self):
        try:
            receita = float(self.entry_receita.get())
            custo = float(self.entry_custo.get())
            lucro_bruto = receita - custo
            margem_lucro = (lucro_bruto / receita) * 100
            self.resultado_lucro.config(text=f"Lucro: R${lucro_bruto:.2f}\nMargem: {margem_lucro:.2f}%")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")

    def calcular_comissao(self):
        try:
            valor_venda = float(self.entry_venda.get())
            taxa_comissao = float(self.entry_comissao.get())
            comissao = valor_venda * (taxa_comissao / 100)
            self.resultado_comissao.config(text=f"Comissão: R${comissao:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceCalculator(root)
    root.mainloop()

