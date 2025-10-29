from calc_corrente import correnteFaseA as correnteFaseAB, correnteFaseB as correnteFaseBC, correnteFaseC as correnteFaseCA


def correnteLinhaA(circuito):
    return correnteFaseAB(circuito) - correnteFaseCA(circuito)


def correnteLinhaB(circuito):
    return correnteFaseBC(circuito) - correnteFaseAB(circuito)


def correnteLinhaC(circuito):
    return correnteFaseCA(circuito) - correnteFaseBC(circuito)
