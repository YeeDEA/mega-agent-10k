import pytest
from agent_collab import (
    calculate_travel_time,
    estimate_energy_consumption,
    compute_population_density,
    predict_traffic_congestion,
    calculate_renewable_share,
    compute_green_space_per_capita,
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

def test_predict_traffic_congestion():
    # normal case
    assert predict_traffic_congestion(100, 50, 1.0) == 2.0
    # with peak factor
    assert predict_traffic_congestion(100, 50, 1.5) == 3.0
    # zero speed safety
    assert predict_traffic_congestion(100, 0, 1.0) == 0.0
    # non‑positive factor safety
    assert predict_traffic_congestion(100, 50, 0) == 0.0

def test_calculate_renewable_share():
    assert calculate_renewable_share(100, 30) == 0.3
    # cap at 1.0
    assert calculate_renewable_share(50, 100) == 1.0
    # zero total energy safety
    assert calculate_renewable_share(0, 10) == 0.0
    # negative inputs safety
    assert calculate_renewable_share(100, -10) == 0.0

def test_compute_green_space_per_capita():
    assert compute_green_space_per_capita(2.0, 1000) == 0.002
    # zero population safety
    assert compute_green_space_per_capita(5.0, 0) == 0.0
    # negative inputs safety
    assert compute_green_space_per_capita(-1.0, 100) == 0.0
