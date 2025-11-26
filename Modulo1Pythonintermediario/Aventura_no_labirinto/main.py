"""
Main do jogo: CLI, loop principal e menu.
Use: python main.py --name Alice --color yellow --dificuldade 1
"""

import argparse
import time
from aventura_pkg import labirinto, jogador, utils
from rich.console import Console
from rich.panel import Panel

console = Console()

def parse_args():
    parser = argparse.ArgumentParser(prog="Aventura no Labirinto", description="Explore o labirinto e vença!")
    parser.add_argument("--name", "-n", required=True, help="Nome do jogador")
    parser.add_argument("--color", "-c", default="yellow", help="Cor principal do jogador")
    parser.add_argument("--dificuldade", "-d", type=int, choices=[1,2,3], default=1, help="Dificuldade (1=pequeno,3=grande)")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa sons do jogo")
    parser.add_argument("--max-movimentos", type=int, default=500, help="Máximo de movimentos permitidos")
    return parser.parse_args()

def tamanho_por_dificuldade(dif):
    if dif == 1:
        return 15, 15
    elif dif == 2:
        return 21, 21
    else:
        return 31, 31

def executar_jogo(args):
    linhas, colunas = tamanho_por_dificuldade(args.dificuldade)
    lab, start, goal = labirinto.criar_labirinto(linhas, colunas, itens=4)
    state = jogador.iniciar_jogador(start)
    state["max_movimentos"] = args.max_movimentos

    # Loop principal simples, lendo teclas com input para maior compatibilidade,
    # mas usamos pynput para possibilitar expansão (ou poderia usar listener).
    utils.imprime_instrucoes()
    console.print(Panel("[bold]Iniciando jogo...[/]"))
    time.sleep(1)

    while True:
        labirinto.imprimir_labirinto(lab, jogador_pos=state["pos"], goal_pos=goal)
        console.print(f"Pontos: {state['pontos']}  Movimentos: {state['movimentos']}/{state['max_movimentos']}")
        console.print("Use W/A/S/D ou as setas para mover. q para menu.")
        key = console.input("[bold cyan]Comando > [/]").strip().lower()

        # traduzir para direções usando match-case
        match key:
            case "w" | "up":
                jogador.mover_jogador(state, lab, "up")
            case "s" | "down":
                jogador.mover_jogador(state, lab, "down")
            case "a" | "left":
                jogador.mover_jogador(state, lab, "left")
            case "d" | "right":
                jogador.mover_jogador(state, lab, "right")
            case "q":
                console.print("Voltando ao menu...")
                break
            case _:
                console.print("Comando não reconhecido.")

        # condições de vitória / derrota
        if state["pos"] == goal:
            jogador.pontuar(state, "chegou")
            labirinto.imprimir_labirinto(lab, jogador_pos=state["pos"], goal_pos=goal)
            console.print(Panel(f"Parabéns, {args.name}! Você venceu com {state['pontos']} pontos!"))
            utils.celebracao_recursiva(6)
            break
        if state["movimentos"] >= state["max_movimentos"]:
            console.print(Panel(f"Fim de movimentos. Você perdeu. Pontos: {state['pontos']}"))
            break

def assistir_solucao(args):
    linhas, colunas = tamanho_por_dificuldade(args.dificuldade)
    lab, start, goal = labirinto.criar_labirinto(linhas, colunas, itens=0)
    path = jogador.soluçao_recursiva(lab, start, goal)
    if not path:
        console.print("Não há solução encontrada.")
        return
    state = jogador.iniciar_jogador(start)
    for pos in path:
        state["pos"] = pos
        labirinto.imprimir_labirinto(lab, jogador_pos=state["pos"], goal_pos=goal)
        time.sleep(0.1)
    console.print("Solução exibida.")

def menu_principal(args):
    while True:
        utils.imprime_menu(args.name)
        choice = console.input("[bold green]Opção > [/]").strip()
        match choice:
            case "1":
                executar_jogo(args)
            case "2":
                utils.imprime_instrucoes()
                console.input("Pressione Enter para voltar.")
            case "3":
                assistir_solucao(args)
                console.input("Pressione Enter para voltar.")
            case "4" | "q":
                console.print("Tchau! Obrigado por jogar.")
                break
            case _:
                console.print("Opção inválida.")

def main():
    args = parse_args()
    menu_principal(args)

if __name__ == "__main__":
    main()
