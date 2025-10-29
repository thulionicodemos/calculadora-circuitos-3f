from imprime_polar import imprimePolar as ip


class Circuito:
    def __init__(
        self,
        fios,
        va,
        vb,
        vc,
        za_linha,
        zb_linha,
        zc_linha,
        za_carga,
        zb_carga,
        zc_carga,
        zn,
    ):
        self.fios = int(fios)
        self.va = complex(va)
        self.vb = complex(vb)
        self.vc = complex(vc)
        self.za_linha = complex(za_linha)
        self.zb_linha = complex(zb_linha)
        self.zc_linha = complex(zc_linha)
        self.za_carga = complex(za_carga)
        self.zb_carga = complex(zb_carga)
        self.zc_carga = complex(zc_carga)
        self.zn = complex(zn)

    def __str__(self):
        return (
            f"Dados do Circuito Trifásico:\n"
            f"Quantidade de fios (3 ou 4): {self.fios}\n"
            f"Tensões: Va = {ip(self.va)}, Vb = {ip(self.vb)}, Vc = {ip(self.vc)}\n"
            f"Impedâncias de linha: Za' = {self.za_linha:.2f}, Zb' = {self.zb_linha:.2f}, Zc' = {self.zc_linha:.2f}\n"
            f"Cargas: Za = {self.za_carga:.2f}, Zb = {self.zb_carga:.2f}, Zc = {self.zc_carga:.2f}\n"
            f"Impedância do neutro: Zn = {self.zn:.2f}\n"
        )

    def calcula_I_n(self):

        I_n = (
            self.va / (self.za_carga + self.za_linha)
            + self.vb / (self.zb_carga + self.zb_linha)
            + self.vc / (self.zc_carga + self.zc_linha)
        ) / (
            1
            + self.zn / (self.za_carga + self.za_linha)
            + self.zn / (self.zb_carga + self.zb_linha)
            + self.zn / (self.zc_carga + self.zc_linha)
        )

        return I_n

    def calcula_V_nl_n(self):

        V_nl_n = (
            self.va / (self.za_carga + self.za_linha)
            + self.vb / (self.zb_carga + self.zb_linha)
            + self.vc / (self.zc_carga + self.zc_linha)
        ) / (
            1 / (self.za_carga + self.za_linha)
            + 1 / (self.zb_carga + self.zb_linha)
            + 1 / (self.zc_carga + self.zc_linha)
        )

        return V_nl_n

    def converteCargaYD(self):

        Z_ab = (
            self.za_carga * self.zb_carga
            + self.zb_carga * self.zc_carga
            + self.zc_carga * self.za_carga
        ) / self.zc_carga

        Z_bc = (
            self.za_carga * self.zb_carga
            + self.zb_carga * self.zc_carga
            + self.zc_carga * self.za_carga
        ) / self.za_carga

        Z_ca = (
            self.za_carga * self.zb_carga
            + self.zb_carga * self.zc_carga
            + self.zc_carga * self.za_carga
        ) / self.zb_carga

        self.za_carga = Z_ab
        self.zb_carga = Z_bc
        self.zc_carga = Z_ca

    def converteCargaDY(self):

        Z_a = (
            self.za_carga
            * self.zc_carga
            / (self.za_carga + self.zb_carga + self.zc_carga)
        )

        Z_b = (
            self.zb_carga
            * self.za_carga
            / (self.za_carga + self.zb_carga + self.zc_carga)
        )

        Z_c = (
            self.zc_carga
            * self.zb_carga
            / (self.za_carga + self.zb_carga + self.zc_carga)
        )

        self.za_carga = Z_a
        self.zb_carga = Z_b
        self.zc_carga = Z_c
