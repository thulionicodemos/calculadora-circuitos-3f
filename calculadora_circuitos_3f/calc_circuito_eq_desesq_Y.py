from calc_corrente import correnteFaseA, correnteFaseB, correnteFaseC
from calc_tensao_carga import tensaoCargaZa, tensaoCargaZb, tensaoCargaZc
from calc_tensao_linha_carga import tensaoLinhaZab, tensaoLinhaZbc, tensaoLinhaZca
from calc_potencia import calculaPotencia, imprimePotencia
from imprime_polar import imprimePolar as ip


def calcula_Y(circuito):

    print("Os resultados do circuito estrela são:\n")

    # Imprimindo os resultados
    if circuito.fios == 3:
        print(f"Vn'n = {ip(circuito.calcula_V_nl_n())}\n")
    else:
        print(f"In = {ip(circuito.calcula_I_n())}\n")

    correntes = (
        correnteFaseA(circuito),
        correnteFaseB(circuito),
        correnteFaseC(circuito),
    )
    tensoes = (
        tensaoCargaZa(circuito),
        tensaoCargaZb(circuito),
        tensaoCargaZc(circuito),
    )
    potencias = calculaPotencia(tensoes, correntes)

    print(f"Ia = {ip(correnteFaseA(circuito))}A")
    print(f"Ib = {ip(correnteFaseB(circuito))}A")
    print(f"Ic = {ip(correnteFaseC(circuito))}A\n")

    print(f"Va'n' = {ip(tensaoCargaZa(circuito))}V")
    print(f"Vb'n' = {ip(tensaoCargaZb(circuito))}V")
    print(f"Vc'n' = {ip(tensaoCargaZc(circuito))}V\n")

    print(f"Va'b' = {ip(tensaoLinhaZab(circuito))}V")
    print(f"Vb'c' = {ip(tensaoLinhaZbc(circuito))}V")
    print(f"Vc'a' = {ip(tensaoLinhaZca(circuito))}V\n")

    imprimePotencia(potencias)
