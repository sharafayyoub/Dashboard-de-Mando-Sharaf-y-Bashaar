def predecir_riesgo(velocidad_media, intensidad_lluvia):
    # Ejemplo simple: ponderación arbitraria
    riesgo = int(0.5 * velocidad_media + 0.8 * intensidad_lluvia)
    if riesgo > 80:
        nivel = "ALTO"
    elif riesgo > 50:
        nivel = "MEDIO"
    else:
        nivel = "BAJO"
    return riesgo, nivel
