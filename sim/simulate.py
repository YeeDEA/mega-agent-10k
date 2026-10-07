import yaml
import argparse
import os
from modules import pipeline, metrics
from modules.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser(description="Run next‑generation simulation")
    parser.add_argument("-c", "--config", default="config.yaml", help="Path to configuration YAML")
    parser.add_argument("-n", "--cycles", type=int, default=1, help="Number of collaboration cycles (version‑2)")
    args = parser.parse_args()

    # Load configuration
    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # Version‑2 orchestration: run multiple cycles using Orchestrator
    orchestrator = Orchestrator(cfg)
    orchestrator.run_cycles(args.cycles)

    print("All cycles completed.")

if __name__ == "__main__":
    main()
