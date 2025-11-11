"""personalizador.painel


Funções para imprimir texto dentro de painéis (rich Panel) com variações.
"""


from typing import Tuple
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from pathlib import Path


console = Console()




def _carregar(texto: str, isArquivo: bool) -> str:
if isArquivo:
p = Path(texto)
if not p.exists():
return f"Arquivo não encontrado: {texto}"
return p.read_text(encoding="utf-8")
return texto




def painel_simples(texto: str, isArquivo: bool = False) -> None:
"""Imprime o texto dentro de um Panel simples com título."""
conteudo = _carregar(texto, isArquivo)
panel = Panel(conteudo, title="Painel Simples", subtitle="personalizador.painel")
console.print(panel)




def painel_com_marcador(texto: str, isArquivo: bool = False) -> None:
"""Imprime o texto dentro de um Panel e adiciona regras (Rule) antes e depois."""
conteudo = _carregar(texto, isArquivo)
console.print(Rule("INÍCIO DO PAINEL"))
panel = Panel(conteudo, title="Painel com marcador", expand=False)
console.print(panel)
console.print(Rule("FIM DO PAINEL"))