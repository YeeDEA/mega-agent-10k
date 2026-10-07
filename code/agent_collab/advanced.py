def predict_traffic_congestion(distance_km: float, avg_speed_kmh: float, peak_factor: float = 1.0) -> float:
    """Estimate travel time under traffic congestion.

    The base travel time is ``distance_km / avg_speed_kmh``. The ``peak_factor``
    scales this time to model rush‑hour effects (e.g. ``1.5`` means 50 % slower).

    Args:
        distance_km: Distance to travel in kilometres.
        avg_speed_kmh: Average speed without congestion.
        peak_factor: Multiplicative factor for congestion. Must be ``>= 1``.

    Returns:
        Adjusted travel time in hours. Returns ``0.0`` if ``avg_speed_kmh`` is
        ``0`` or ``peak_factor`` is non‑positive.
    """
    if avg_speed_kmh == 0 or peak_factor <= 0:
        return 0.0
    base_time = distance_km / avg_speed_kmh
    return base_time * peak_factor

def calculate_renewable_share(total_energy_kwh: float, renewable_energy_kwh: float) -> float:
    """Return the proportion of renewable energy (0‑1).

    Args:
        total_energy_kwh: Total energy consumption.
        renewable_energy_kwh: Amount supplied by renewable sources.

    Returns:
        Fraction of renewable energy. Returns ``0.0`` if ``total_energy_kwh`` is
        ``0`` or any argument is negative.
    """
    if total_energy_kwh <= 0 or renewable_energy_kwh < 0:
        return 0.0
    share = renewable_energy_kwh / total_energy_kwh
    return min(max(share, 0.0), 1.0)

def compute_green_space_per_capita(green_area_km2: float, population: int) -> float:
    """Calculate green space per person (km² per capita).

    Args:
        green_area_km2: Total green area in square kilometres.
        population: Number of inhabitants.

    Returns:
        Green space per capita. Returns ``0.0`` if ``population`` is ``0`` or if
        any argument is negative.
    """
    if population <= 0 or green_area_km2 < 0:
        return 0.0
    return green_area_km2 / population
