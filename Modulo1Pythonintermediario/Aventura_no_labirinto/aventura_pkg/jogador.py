"""
Módulo jogador: controle do jogador, movimento e pontuação.

Funções:
- iniciar_jogador(lab, start): retorna estado do jogador
- mover_jogador(state, direção): tenta mover o jogador e atualizar pontuação
- pontuar(state, evento): atualiza pontos
- soluçao_recursiva(lab, start, goal): função recursiva que encontra caminho (DFS)
"""

from typing import Tuple, List, Dict
from pynput import keyboard
from .labirinto import FREE, WALL, ITEM
import time

def iniciar_jogador(start: Tuple[int,int]):
    """
    Inicializa o estado do jogador.
    state: dict com posição, pontos, histórico de movimentos
    """
    state = {
        "pos": start,
        "pontos": 0,
        "movimentos": 0,
        "itens_coletados": 0,
        "max_movimentos": 1000
    }
    return state

def pontuar(state: Dict, evento: str):
    """
    Atualiza pontuação baseando-se no evento:
    - 'coletou_item' -> +10
    - 'mover' -> -1
    - 'chegou' -> +50
    """
    if evento == "coletou_item":
        state["pontos"] += 10
        state["itens_coletados"] += 1
    elif evento == "mover":
        state["pontos"] -= 1
    elif evento == "chegou":
        state["pontos"] += 50

def mover_jogador(state: Dict, lab, direcao: str):
    """
    Tenta mover o jogador na direção ('up','down','left','right').
    Retorna True se a posição mudou.
    """
    r, c = state["pos"]
    offsets = {
        "up": (-1,0),
        "down": (1,0),
        "left": (0,-1),
        "right": (0,1)
    }
    if direcao not in offsets:
        return False
    dr, dc = offsets[direcao]
    nr, nc = r + dr, c + dc

    # limites
    if nr < 0 or nr >= len(lab) or nc < 0 or nc >= len(lab[0]):
        return False
    # parede?
    if lab[nr][nc] == WALL:
        return False

    # mover
    state["pos"] = (nr, nc)
    state["movimentos"] += 1
    pontuar(state, "mover")

    # coletar item?
    if lab[nr][nc] == ITEM:
        lab[nr][nc] = FREE
        pontuar(state, "coletou_item")
    return True

def soluçao_recursiva(lab, start, goal):
    """
    Função recursiva (DFS) que encontra um caminho de start -> goal.
    Retorna lista de posições (ou None se não encontrado).
    """
    visited = set()
    path = []

    def dfs(pos):
        if pos == goal:
            path.append(pos)
            return True
        r, c = pos
        visited.add(pos)
        # vizinhos: priorize ordem (down,right,up,left) só como exemplo
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < len(lab) and 0 <= nc < len(lab[0]) and lab[nr][nc] != WALL and (nr,nc) not in visited:
                if dfs((nr,nc)):
                    path.append(pos)
                    return True
        return False

    found = dfs(start)
    if not found:
        return None
    return list(reversed(path))
