"""
Módulo utils: utilitários como impressão de menu, instruções e celebração recursiva.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import time

console = Console()

def imprime_instrucoes(path_instrucoes: str = None):
    """
    Lê instruções de arquivo (se fornecido) e imprime formatado.
    Se path_instrucoes for None, imprime instruções padrão.
    """
    text = ""
    if path_instrucoes:
        try:
            with open(path_instrucoes, "r", encoding="utf-8") as f:
                text = f.read()
        except FileNotFoundError:
            text = "Arquivo de instruções não encontrado. Usando instruções padrão.\n"
    if not text:
        text = (
            "Aventura no Labirinto\n\n"
            "Movimente-se com as setas ou WASD.\n"
            "Colete itens (●) para ganhar pontos.\n"
            "Chegar em G vence o jogo.\n"
        )
    console.print(Panel(text, title="Instruções"))

def imprime_menu(name: str = "Jogador"):
    """
    Imprime um menu simples usando match-case no main.
    """
    console.print(Panel(f"Bem-vindo, {name}! Escolha uma opção:\n1 - Jogar\n2 - Instruções\n3 - Solução automática\n4 - Sair", title="Menu"))

def celebracao_recursiva(n: int):
    """
    Animação recursiva simples de celebração: imprime n estrelas (recursivamente).
    """
    if n <= 0:
        return
    console.print("✨ " * n)
    time.sleep(0.2)
    celebracao_recursiva(n-1)
