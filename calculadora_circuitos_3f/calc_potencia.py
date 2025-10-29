import numpy as np


def calculaPotencia(tensoes, correntes):

    # Potência em cada fase
    S_fases = {
        "A": tensoes[0] * np.conj(correntes[0]),
        "B": tensoes[1] * np.conj(correntes[1]),
        "C": tensoes[2] * np.conj(correntes[2]),
    }

    # P (ativa), Q (reativa) e |S| (aparente) por fase
    P_fases = {fase: np.real(S) for fase, S in S_fases.items()}
    Q_fases = {fase: np.imag(S) for fase, S in S_fases.items()}
    S_aparente_fases = {fase: np.abs(S) for fase, S in S_fases.items()}

    # Soma total
    S_total = sum(S_fases.values())
    P_total = np.real(S_total)
    Q_total = np.imag(S_total)
    S_aparente_total = np.abs(S_total)

    # Fator de potência
    fp = P_total / S_aparente_total
    if Q_total > 0:
        tipo_fp = "atrasado (indutivo)"
    elif Q_total < 0:
        tipo_fp = "adiantado (capacitivo)"

    resultados = {
        "S_fases": S_fases,
        "P_fases": P_fases,
        "Q_fases": Q_fases,
        "S_aparente_fases": S_aparente_fases,
        "S_total": S_total,
        "P_total": P_total,
        "Q_total": Q_total,
        "S_aparente_total": S_aparente_total,
        "fp": fp,
        "tipo_fp": tipo_fp,
    }

    return resultados


def imprimePotencia(potencias):

    print("Potências:\n")
    print("Fase A:")
    print(f"    Sa = {potencias['S_fases']['A']:.2f}")
    print(f"    Pa = {potencias['P_fases']['A']:.2f}W")
    print(f"    Qa = {potencias['Q_fases']['A']:.2f}VAr")
    print(f"    |Sa| = {potencias['S_aparente_fases']['A']:.2f}VA\n")

    print("Fase B:")
    print(f"    Sb = {potencias['S_fases']['B']:.2f}")
    print(f"    Pb = {potencias['P_fases']['B']:.2f}W")
    print(f"    Qb = {potencias['Q_fases']['B']:.2f}VAr")
    print(f"    |Sb| = {potencias['S_aparente_fases']['B']:.2f}VA\n")

    print("Fase C:")
    print(f"    Sc = {potencias['S_fases']['C']:.2f}")
    print(f"    Pc = {potencias['P_fases']['C']:.2f}W")
    print(f"    Qc = {potencias['Q_fases']['C']:.2f}VAr")
    print(f"    |Sc| = {potencias['S_aparente_fases']['C']:.2f}VA\n")

    print("Total:")
    print(f"    S = {potencias['S_total']:.2f}")
    print(f"    P = {potencias['P_total']:.2f}W")
    print(f"    Q = {potencias['Q_total']:.2f}VAr")
    print(f"    |S| = {potencias['S_aparente_total']:.2f}VA\n")

    print("Fator de Potência:")
    print(f"    fp = {potencias['fp']:.2f}")
    print(f"    Tipo: {potencias['tipo_fp']}\n")
