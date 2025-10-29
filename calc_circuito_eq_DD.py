from calc_corrente import (
    correnteFaseA as Iab,
    correnteFaseB as Ibc,
    correnteFaseC as Ica,
)
from calc_corrente_linha_carga import (
    correnteLinhaA as Ia,
    correnteLinhaB as Ib,
    correnteLinhaC as Ic,
)
from calc_tensao_carga import (
    tensaoCargaZa as Va,
    tensaoCargaZb as Vb,
    tensaoCargaZc as Vc,
)
from imprime_polar import imprimePolar as ip


def calcula_D_equilibrado(circuito):

    print("Os resultados do circuito triângulo equilibrado são:\n")

    # Imprimindo os resultados
    print("Como a configuração é triangulo, as tensões de linha e de fase são iguais.")
    print(f"Va'n' = {ip(Va(circuito))}")
    print(f"Vb'n' = {ip(Vb(circuito))}")
    print(f"Vc'n' = {ip(Vc(circuito))}\n")

    print(f"Ia'b' = {ip(Iab(circuito))}")
    print(f"Ib'c' = {ip(Ibc(circuito))}A")
    print(f"Ic'a' = {ip(Ica(circuito))}A\n")

    print(f"Ia = {ip(Ia(circuito))}")
    print(f"Ib = {ip(Ib(circuito))}")
    print(f"Ic = {ip(Ic(circuito))}\n")
