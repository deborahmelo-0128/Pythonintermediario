"""
Módulo labirinto: geração e impressão do labirinto.

Contém:
- criar_labirinto(dificuldade): gera um labirinto usando backtracking (função recursiva).
- imprimir_labirinto(lab): imprime usando rich.
- gerar_labirinto_vazio(linhas, colunas): utilitário.
"""

from random import shuffle, randrange
from rich.console import Console

console = Console()

WALL = 1
FREE = 0
PLAYER = "P"
GOAL = "G"
ITEM = "I"

def gerar_labirinto_vazio(linhas: int, colunas: int):
    """
    Gera uma matriz com paredes e células livres (todas paredes iniciais).
    As dimensões consideradas para o algoritmo usam grades ímpares para caminhos.
    """
    grid = [[WALL for _ in range(colunas)] for _ in range(linhas)]
    return grid

def criar_labirinto(linhas: int = 21, colunas: int = 21, itens: int = 3):
    """
    Cria um labirinto usando recursive backtracking (função recursiva).
    Retorna a matriz, posição inicial do jogador e posição da meta.
    """
    if linhas % 2 == 0: linhas += 1
    if colunas % 2 == 0: colunas += 1

    grid = gerar_labirinto_vazio(linhas, colunas)

    # Células visitadas: marcamos caminhos como FREE
    def carve(r, c):
        """
        Função recursiva que "cava" caminhos a partir da célula (r, c).
        """
        grid[r][c] = FREE
        dirs = [(0,2),(0,-2),(2,0),(-2,0)]
        shuffle(dirs)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 1 <= nr < linhas-1 and 1 <= nc < colunas-1 and grid[nr][nc] == WALL:
                # remover parede entre (r,c) e (nr,nc)
                grid[r + dr//2][c + dc//2] = FREE
                carve(nr, nc)

    # começar em (1,1)
    carve(1,1)

    # colocar jogador e objetivo
    start = (1,1)
    goal = (linhas-2, colunas-2)

    # colocar alguns items aleatórios em células livres
    free_cells = [(r,c) for r in range(1,linhas-1) for c in range(1,colunas-1) if grid[r][c]==FREE and (r,c) not in [start,goal]]
    shuffle(free_cells)
    for i in range(min(itens, len(free_cells))):
        r,c = free_cells[i]
        grid[r][c] = ITEM

    return grid, start, goal

def imprimir_labirinto(lab, jogador_pos=None, goal_pos=None):
    """
    Imprime o labirinto no terminal com a biblioteca rich.
    lab: matriz de inteiros e possivelmente 'I' para item
    jogador_pos: (r,c), goal_pos: (r,c)
    """
    rows = []
    for r, row in enumerate(lab):
        line = ""
        for c, cell in enumerate(row):
            if jogador_pos == (r,c):
                line += "[bold yellow]P[/] "
            elif goal_pos == (r,c):
                line += "[bold green]G[/] "
            elif cell == WALL:
                line += "█ "
            elif cell == FREE:
                line += "  "
            elif cell == ITEM:
                line += "[magenta]●[/] "
            else:
                line += "  "
        rows.append(line)
    console.clear()
    for ln in rows:
        console.print(ln)

