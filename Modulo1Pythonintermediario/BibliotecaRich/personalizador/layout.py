"""personalizador.layout


Funções para demonstrar utilitários de *layout* do rich.
Cada função recebe (texto: str, isArquivo: bool) e imprime o texto
ou o conteúdo do arquivo usando componentes do rich.layout e rich.console.
"""


from typing import Tuple
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from pathlib import Path


console = Console()




def _carregar(texto: str, isArquivo: bool) -> str:
"""Carrega conteúdo: se isArquivo True, lê o arquivo; senão retorna a string."""
if isArquivo:
p = Path(texto)
if not p.exists():
return f"Arquivo não encontrado: {texto}"
return p.read_text(encoding="utf-8")
return texto




def mostrar_em_layout(texto: str, isArquivo: bool = False) -> None:
"""Mostra o texto em um layout dividido em cabeçalho / corpo.


Args:
texto: string ou caminho de arquivo
isArquivo: se True, interpreta `texto` como caminho
"""
conteudo = _carregar(texto, isArquivo)
layout = Layout()
layout.split_column(
Layout(name="header", size=3),
Layout(name="body", ratio=2),
Layout(name="footer", size=3),
)


layout["header"].update(Panel("[bold]HEADER[/bold] - Exemplo de Layout"))
layout["body"].update(Panel(conteudo, title="Conteúdo"))
layout["footer"].update(Panel("Footer — gerado por personalizador.layout"))


console.print(layout)




def mostrar_em_duas_colunas(texto: str, isArquivo: bool = False) -> None:
"""Divide a tela em duas colunas e imprime o conteúdo em ambas para demonstrar "espelhamento".


Útil para ver efeitos de alinhamento e largura.
"""
conteudo = _carregar(texto, isArquivo)
layout = Layout()
left = Layout(name="left")
right = Layout(name="right")
layout.split_row(left, right)


left.update(Panel(conteudo, title="Esquerda"))
right.update(Panel(conteudo[: max(1, len(conteudo)//2)], title="Direita — metade"))


console.print(layout)