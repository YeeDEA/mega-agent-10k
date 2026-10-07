import yaml
import argparse
import os
from modules import pipeline, metrics

def main():
    parser = argparse.ArgumentParser(description="Run next‑generation simulation")
    parser.add_argument("-c", "--config", default="config.yaml", help="Path to configuration YAML")
    parser.add_argument("-r", "--run", default="Run1", help="Name of the experiment run to execute")
    args = parser.parse_args()

    # Load configuration
    with open(args.config, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    # Initialize agents and pipeline
    sim = pipeline.Simulation(cfg)
    sim.run(run_name=args.run)

    # After simulation, compute metrics
    results = metrics.compute_all(sim)
    # Export results
    output_dir = os.path.join("output", args.run)
    os.makedirs(output_dir, exist_ok=True)
    results.to_csv(os.path.join(output_dir, "metrics.csv"), index=False)
    print(f"Simulation completed. Metrics saved to {output_dir}")

if __name__ == "__main__":
    main()
