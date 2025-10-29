from calc_circuito_eq_desesq_Y import calcula_Y
from calc_circuito_eq_DD import calcula_D_equilibrado
from calc_circuito_deseq_D import calcula_D_deseq
import convert as cv
from circuito_trifasico import Circuito


def main():

    ### Escolha do tipo de circuito
    print("Escolha o tipo de circuito:")
    print("1 - Circuito Y (estrela) - Pode ser equilibrado ou desequilibrado")
    print("2 - Circuito Δ (triângulo) equilibrado")
    print("3 - Circuito Δ (triângulo) desequilibrado")

    while True:
        try:
            escolha = int(input("Digite o número da opção (1, 2 ou 3): "))
            if escolha in [1, 2, 3]:
                break
            else:
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    ### Dados do circuito
    # Entrar com a tensão de fase-neutro da fonte
    Va = Vb = Vc = 127
    angulo_Va = 30
    angulo_Vb = angulo_Va + 120
    angulo_Vc = angulo_Va - 120

    circuito = Circuito(
        fios=3,
        va=cv.polar_to_rect(Va, angulo_Va),
        vb=cv.polar_to_rect(Vb, angulo_Vb),
        vc=cv.polar_to_rect(Vc, angulo_Vc),
        za_linha=(0.4 + 0.8j) * 25,
        zb_linha=(0.4 + 0.8j) * 25,
        zc_linha=(0.4 + 0.8j) * 25,
        za_carga=10 + 7j,
        zb_carga=20 - 10j,
        zc_carga=20 + 20j,
        zn=0,
    )
    ###################################################
    print(circuito)

    # Chama a função apropriada baseada na escolha
    if escolha == 1:
        calcula_Y(circuito)
    elif escolha == 2:
        calcula_D_equilibrado(circuito)
    elif escolha == 3:
        calcula_D_deseq(circuito)


if __name__ == "__main__":
    main()
