"""Top-level package for agent_collab.

Provides convenient imports for the stub modules.
"""

from .transport import calculate_travel_time
from .energy import estimate_energy_consumption
from .urban import compute_population_density

__all__ = [
    "calculate_travel_time",
    "estimate_energy_consumption",
    "compute_population_density",
]
