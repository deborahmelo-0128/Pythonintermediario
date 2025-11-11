"""
Pacote aventura_pkg: contém a lógica do labirinto, controle do jogador e utilitários.
"""
from .labirinto import criar_labirinto, imprimir_labirinto, gerar_labirinto_vazio
from .jogador import iniciar_jogador, mover_jogador, pontuar, soluçao_recursiva
from .utils import imprime_instrucoes, imprime_menu, celebracao_recursiva
