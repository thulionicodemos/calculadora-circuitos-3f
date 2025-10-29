from convert import polar_to_rect
from calc_corrente import correnteFaseA, correnteFaseB, correnteFaseC
from imprime_polar import imprimePolar as ip
from calc_potencia import calculaPotencia, imprimePotencia


# Perguntar por que nao da certo para equilibrados
def calcula_D_deseq(circuito):

    zabOriginal = circuito.za_carga
    zbcOriginal = circuito.zb_carga
    zcaOriginal = circuito.zc_carga

    circuito.converteCargaDY()

    I_a = correnteFaseA(circuito)
    I_b = correnteFaseB(circuito)
    I_c = correnteFaseC(circuito)

    # print(f"***{ip(I_a)}, {ip(I_b)}, {ip(I_c)}***\n")

    V_al = circuito.va - I_a * circuito.za_linha
    V_bl = circuito.vb - I_b * circuito.zb_linha
    V_cl = circuito.vc - I_c * circuito.zc_linha

    # print(f"***{ip(V_al)}, {ip(V_bl)}, {ip(V_cl)}***\n")

    V_albl = V_al - V_bl
    V_blcl = V_bl - V_cl
    V_clal = V_cl - V_al

    # print(f"***{ip(V_albl)}, {ip(V_blcl)}, {ip(V_clal)}***\n")

    I_ab = V_albl / zabOriginal
    I_bc = V_blcl / zbcOriginal
    I_ca = V_clal / zcaOriginal

    correntes_carga = (
        I_ab,
        I_bc,
        I_ca,
    )
    tensoes_carga = (
        V_albl,
        V_blcl,
        V_clal,
    )

    correntes_linha = (
        I_a,
        I_b,
        I_c,
    )
    tensoes_linha = (
        I_a * circuito.za_linha,
        I_b * circuito.zb_linha,
        I_c * circuito.zc_linha,
    )

    potencias_carga = calculaPotencia(tensoes_carga, correntes_carga)
    potencias_linha = calculaPotencia(tensoes_linha, correntes_linha)

    print("Os resultados do circuito Triângulo Desequilibrado são:\n")

    print(f"Ia = {ip(I_a)}")
    print(f"Ib = {ip(I_b)}")
    print(f"Ic = {ip(I_c)}\n")

    print(f"Iab = {ip(I_ab)}")
    print(f"Ibc = {ip(I_bc)}")
    print(f"Ica = {ip(I_ca)}\n")

    print(f"Va'b' = {ip(V_albl)}")
    print(f"Vb'c' = {ip(V_blcl)}")
    print(f"Vc'a' = {ip(V_clal)}\n")

    print("P carga")
    imprimePotencia(potencias_carga)

    print("P linha")
    imprimePotencia(potencias_linha)
