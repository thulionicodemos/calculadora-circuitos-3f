def correnteFaseA(circuito):
    impedancia_total_a = circuito.za_linha + circuito.za_carga
    I_n = circuito.calcula_I_n()
    V_nl_n = circuito.calcula_V_nl_n()

    if impedancia_total_a == 0:
        return "Impedância total na fase A é nula"

    elif circuito.fios == 3:
        return circuito.va / impedancia_total_a - V_nl_n / impedancia_total_a
    else:
        return circuito.va / impedancia_total_a - I_n * circuito.zn / impedancia_total_a


def correnteFaseB(circuito):
    impedancia_total_b = circuito.zb_linha + circuito.zb_carga
    I_n = circuito.calcula_I_n()
    V_nl_n = circuito.calcula_V_nl_n()

    if impedancia_total_b == 0:
        return "Impedância total na fase B é nula"

    elif circuito.fios == 3:
        return circuito.vb / impedancia_total_b - V_nl_n / impedancia_total_b
    else:
        return circuito.vb / impedancia_total_b - I_n * circuito.zn / impedancia_total_b


def correnteFaseC(circuito):
    impedancia_total_c = circuito.zc_linha + circuito.zc_carga
    I_n = circuito.calcula_I_n()
    V_nl_n = circuito.calcula_V_nl_n()

    if impedancia_total_c == 0:
        return "Impedância total na fase C é nula"

    elif circuito.fios == 3:
        return circuito.vc / impedancia_total_c - V_nl_n / impedancia_total_c
    else:
        return circuito.vc / impedancia_total_c - I_n * circuito.zn / impedancia_total_c
