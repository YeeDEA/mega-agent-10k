import pytest
from agent_collab import (
    calculate_travel_time,
    estimate_energy_consumption,
    compute_population_density,
)

def test_calculate_travel_time():
    assert calculate_travel_time(100, 50) == 2.0
    assert calculate_travel_time(0, 10) == 0.0
    assert calculate_travel_time(10, 0) == 0.0  # avoid division by zero

def test_estimate_energy_consumption():
    assert estimate_energy_consumption(5, 3) == 15.0
    assert estimate_energy_consumption(-1, 3) == 0.0
    assert estimate_energy_consumption(5, -2) == 0.0

def test_compute_population_density():
    assert compute_population_density(1000, 2) == 500.0
    assert compute_population_density(0, 10) == 0.0
    assert compute_population_density(100, 0) == 0.0
    assert compute_population_density(-5, 10) == 0.0
