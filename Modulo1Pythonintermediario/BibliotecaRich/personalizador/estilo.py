"""personalizador.estilo


Funções que aplicam estilos (markup do rich) ao texto e o imprimem.
"""


from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from pathlib import Path


console = Console()




def _carregar(texto: str, isArquivo: bool) -> str:
if isArquivo:
p = Path(texto)
if not p.exists():
return f"Arquivo não encontrado: {texto}"
return p.read_text(encoding="utf-8")
return texto




def estilo_markdown(texto: str, isArquivo: bool = False) -> None:
"""Interpreta o texto como markdown e renderiza com rich.Markdown."""
conteudo = _carregar(texto, isArquivo)
md = Markdown(conteudo)
console.print(md)




def estilo_colorido(texto: str, isArquivo: bool = False) -> None:
"""Aplica estilos inline (bold, italic, color) usando rich.Text e markup."""
conteudo = _carregar(texto, isArquivo)
t = Text(conteudo)
# exemplo simples de transformação: palavras curtas em bold, palavras longas em italic
for palavra in conteudo.split():
if len(palavra) <= 3:
t.highlight_words([palavra], style="bold")
elif len(palavra) > 7:
t.highlight_words([palavra], style="italic")
console.print(t)