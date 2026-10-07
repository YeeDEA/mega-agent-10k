# Simulation Pipeline Overview

This repository contains the implementation of the **next‑generation simulation** based on the approved specification.

## Directory Layout
```
 demo_site/
 └─ sim/
    ├─ README.md          # This documentation (pipeline overview)
    ├─ config.yaml        # Simulation parameters and tunables
    ├─ simulate.py        # Core driver script (Python)
    ├─ run_simulation.ps1 # PowerShell wrapper to execute the simulation
    └─ modules/
        ├─ agents.py      # Agent definitions and group behaviours
        ├─ metrics.py     # Metric calculations (IIS, NRI, CE, MCR)
        └─ pipeline.py    # Orchestration of simulation steps
```

## Pipeline Steps (as described in the spec)
1. **Initialize Agents** – Load the base 10 000 agents and assign 3 % to the new groups (Catalysts, Guardians, Explorers, Collaborators, Regulators).
2. **Run Baseline Simulation** – Execute the original simulation for the defined period.
3. **Inject Group Behaviours** – Activate Catalyst amplification, Guardian suppression, Explorer seeding, Collaborator co‑creation, and Regulator throttling.
4. **Collect Metrics** – Compute the extended metrics (IIS, NRI, CE, MCR, Resource Utilization).
5. **Generate Reports** – Output CSVs and visual heatmaps for analysis.
6. **Iterate Parameters** – Optionally sweep over catalyst factors, guardian thresholds, and regulator policies.

The `run_simulation.ps1` script ties everything together and can be invoked with optional arguments to select a specific experiment run (e.g., `-Run 1`).

---

### Getting Started
```powershell
# Navigate to the simulation directory
cd C:\Users\user1\.gemini\antigravity\scratch\demo_site\sim

# Install required Python packages (if not already installed)
python -m pip install -r requirements.txt

# Execute the default run (Run 1)
.un_simulation.ps1 -Run 1
```

---

**Contact**: For academic collaborations or industry partnerships, please reach out to the simulation team lead.
