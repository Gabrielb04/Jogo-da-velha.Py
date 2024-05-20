import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.configure(bg="#000000")

        self.turno = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for linha in range(3):
            for coluna in range(3):
                self.botoes[linha][coluna] = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2, bg="#333333", fg="#FFFFFF", command=lambda linha=linha, coluna=coluna: self.jogada(linha, coluna))
                self.botoes[linha][coluna].grid(row=linha, column=coluna, padx=5, pady=5)

    def jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == "":
            self.tabuleiro[linha][coluna] = self.turno
            self.botoes[linha][coluna].config(text=self.turno, fg="#FF0000" if self.turno == "X" else "#FFFFFF")
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"O jogador {self.turno} venceu!")
                self.resetar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.resetar_jogo()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_vitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != "":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != "":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != "":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != "":
            return True
        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            for elemento in linha:
                if elemento == "":
                    return False
        return True

    def resetar_jogo(self):
        for linha in range(3):
            for coluna in range(3):
                self.tabuleiro[linha][coluna] = ""
                self.botoes[linha][coluna].config(text="")
        self.turno = "X"

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
