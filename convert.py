import numpy as np

# Converte um número na forma polar para forma retângular
def polar_to_rect(r, angulo):

    theta = np.deg2rad(angulo)
    z = r * np.exp(1j * theta) # essa linha utiliza a fórmula de Euler -> e^jθ = cosθ + jsinθ e multiplica a soma pelo raio que retorna o numero complexo na forma retângular

    return z

# Converte um número na forma retângular para forma polar
def rect_to_polar(Z):

    r = np.abs(Z)
    angulo = np.angle(Z, deg = True) # Converte o angulo do numero complexo em radianos e de radianos para graus

    return r, angulo