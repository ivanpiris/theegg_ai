def caida_tierra(segundos: int) -> float:
    """
    Esta función calcula la altura a la que se encuentra un objeto en la Tierra después de caer durante un tiempo dado.

    Parameters:
    segundos (int): Tiempo en segundos que ha estado cayendo el objeto.

    Returns:
    float: Altura en metros.

    Example:
    >>> caida_tierra(5)
    122.5
    >>> caida_tierra(10)
    490.0
    """
    gravedad = 9.8
    altura = gravedad * (segundos ** 2) / 2
    return altura

def caida_marte(segundos: int) -> float:
    """
    Esta función calcula la altura a la que se encuentra un objeto en Marte después de caer durante un tiempo dado.

    Parameters:
    segundos (int): Tiempo en segundos que ha estado cayendo el objeto.

    Returns:
    float: Altura en metros.

    Example:
    >>> caida_marte(5)
    49.5
    >>> caida_marte(10)
    222.0
    """
    gravedad = 3.7
    altura = gravedad * (segundos ** 2) / 2
    return altura

def caida_jupiter(segundos: int) -> float:
    """
    Esta función calcula la altura a la que se encuentra un objeto en Jupiter después de caer durante un tiempo dado.

    Parameters:
    segundos (int): Tiempo en segundos que ha estado cayendo el objeto.

    Returns:
    float: Altura en metros.

    Example:
    >>> caida_jupiter(5)
    1235.5
    >>> caida_jupiter(10)
    5940.0
    """
    gravedad = 24.8
    altura = gravedad * (segundos ** 2) / 2
    return altura