def estimate_energy_consumption(power_kw: float, hours: float) -> float:
    """Estimate energy consumption in kilowatt‑hours.

    Args:
        power_kw: Power rating in kilowatts.
        hours: Operating time in hours.

    Returns:
        Energy consumption (kWh). Returns ``0.0`` if either argument is negative.
    """
    if power_kw < 0 or hours < 0:
        return 0.0
    return power_kw * hours
