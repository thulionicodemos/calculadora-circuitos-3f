from calc_tensao_carga import tensaoCargaZa, tensaoCargaZb, tensaoCargaZc


def tensaoLinhaZab(circuito):
    return tensaoCargaZa(circuito) - tensaoCargaZb(circuito)


def tensaoLinhaZbc(circuito):
    return tensaoCargaZb(circuito) - tensaoCargaZc(circuito)


def tensaoLinhaZca(circuito):
    return tensaoCargaZc(circuito) - tensaoCargaZa(circuito)
