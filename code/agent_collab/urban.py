def compute_population_density(population: int, area_km2: float) -> float:
    """Compute population density (people per square kilometre).

    Args:
        population: Number of people.
        area_km2: Area in square kilometres.

    Returns:
        Density as ``population / area_km2``. Returns ``0.0`` if ``area_km2``
        is ``0`` to avoid division by zero or if ``population`` is negative.
    """
    if area_km2 == 0 or population < 0:
        return 0.0
    return population / area_km2
