"""personalizador.progresso


Funções que demonstram barras de progresso do rich. Aqui usamos um hack: quando o
argumento `texto` for curto (ex.: uma frase) a função fará um loop para simular
processamento e mostrar a barra. Se `isArquivo` for True, lemos linhas do arquivo e
as processamos com barra de progresso.
"""


from typing import Iterable
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeRemainingColumn
from pathlib import Path
import time


console = Console()




def _carregar_linhas(texto: str, isArquivo: bool):
if isArquivo:
p = Path(texto)
if not p.exists():
return [f"Arquivo não encontrado: {texto}"]
return p.read_text(encoding="utf-8").splitlines() or [""]
# se não for arquivo, splits por frase (ponto) para criar "trabalho" simulado
return [l.strip() for l in texto.split('.') if l.strip()]




def progresso_simples(texto: str, isArquivo: bool = False) -> None:
"""Mostra uma barra de progresso que itera sobre partes do texto."""
linhas = _carregar_linhas(texto, isArquivo)
with Progress("{task.description}", SpinnerColumn(), BarColumn(), "[progress.percentage]{task.percentage:>3.0f}%", TimeRemainingColumn()) as progress:
task = progress.add_task("Processando", total=len(linhas))
for linha in linhas:
# simula trabalho
time.sleep(0.15)
progress.update(task, advance=1)
console.print("[green]Concluído![/green]")




def progresso_com_texto(texto: str, isArquivo: bool = False) -> None:
"""Mostra progresso e exibe cada 'unidade' processada em tempo real."""
linhas = _carregar_linhas(texto, isArquivo)
with Progress(TextColumn("{task.fields[nome]}"), BarColumn(), "{task.percentage:>3.0f}%") as progress:
task = progress.add_task("convertendo", total=len(linhas), nome="---")
for i, linha in enumerate(linhas, 1):
time.sleep(0.12)
progress.update(task, advance=1, nome=(linha[:40] + "...") if len(linha) > 40 else linha)
console.print("[bold]Processamento finalizado.[/bold]")