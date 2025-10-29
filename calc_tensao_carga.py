from calc_corrente import correnteFaseA, correnteFaseB, correnteFaseC


def tensaoCargaZa(circuito):
    return correnteFaseA(circuito) * circuito.za_carga


def tensaoCargaZb(circuito):
    return correnteFaseB(circuito) * circuito.zb_carga


def tensaoCargaZc(circuito):
    return correnteFaseC(circuito) * circuito.zc_carga
