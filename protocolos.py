PROTOCOLOS = {
    "VÍSPERA": {
        "disparador": "Condiciones normales, vigilancia preventiva.",
        "acciones": "Monitorizar sensores, preparar equipos, comunicación estándar."
    },
    "CÓDIGO ROJO": {
        "disparador": "Viento > 90 km/h o Inundación > 100 cm.",
        "acciones": "Activar refugios, cortar suministros, alerta máxima."
    },
    "RENACIMIENTO": {
        "disparador": "Descenso de riesgo tras evento crítico.",
        "acciones": "Evaluar daños, iniciar recuperación, restablecer servicios."
    }
}

def detectar_protocolo(viento, inundacion):
    if viento > 90 or inundacion > 100:
        return "CÓDIGO ROJO: TITÁN"
    elif viento < 40 and inundacion < 30:
        return "VÍSPERA"
    else:
        return "RENACIMIENTO"
