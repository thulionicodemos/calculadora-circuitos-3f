import convert as cv


# Recebe um valor na forma retangular e imprime na forma polar
def imprimePolar(valor_retangular):

    return f"{cv.rect_to_polar(valor_retangular)[0]:.2f} |_{cv.rect_to_polar(valor_retangular)[1]:.2f}°"
