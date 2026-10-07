import os
import pandas as pd
from .pipeline import Simulation
from . import metrics

class Orchestrator:
    """Version‑2 orchestration layer.
    
    Executes the core ``Simulation`` for a number of *collaboration cycles*.
    After each cycle it computes metrics and writes them to ``output/CycleX/metrics.csv``.
    This mimics a multi‑round corporate workflow where results are reviewed
    and persisted before the next iteration.
    """
    def __init__(self, cfg):
        self.cfg = cfg

    def run_cycles(self, num_cycles: int = 1):
        for i in range(1, num_cycles + 1):
            sim = Simulation(self.cfg)
            sim.run(run_name=f"Cycle{i}")

            # Compute and persist metrics for this cycle
            results = metrics.compute_all(sim)
            output_dir = os.path.join("output", f"Cycle{i}")
            os.makedirs(output_dir, exist_ok=True)
            results.to_csv(os.path.join(output_dir, "metrics.csv"), index=False)
            print(f"Cycle {i} completed. Metrics saved to {output_dir}")
