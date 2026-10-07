def calculate_travel_time(distance_km: float, speed_kmh: float) -> float:
    """Calculate travel time in hours.

    Args:
        distance_km: Distance to travel in kilometers.
        speed_kmh: Average speed in kilometers per hour.

    Returns:
        Travel time in hours. Returns ``0.0`` if ``speed_kmh`` is 0 to avoid
        division by zero.
    """
    if speed_kmh == 0:
        return 0.0
    return distance_km / speed_kmh
