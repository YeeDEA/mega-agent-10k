import os
import sys
import pytest
from pathlib import Path

# Add sim to sys.path
SIM_DIR = Path(__file__).resolve().parent.parent.parent / "sim"
sys.path.insert(0, str(SIM_DIR))

from modules.v2_resilience import OrganizationHierarchy, QualityGate, AdversarialEngine, ExecutiveSummarizer

def test_v2_organization_hierarchy_construction():
    """Verify 2 Divisions, 10 Labs, 100 Teams, and 1,000 agents in quick mode."""
    divisions, all_agents = OrganizationHierarchy.build(agents_per_team=10)
    assert len(divisions) == 2
    assert len(all_agents) == 1000
    
    total_teams = sum(len(lab.teams) for div in divisions for lab in div.labs)
    assert total_teams == 100

def test_v2_quality_gate_inspection_and_healing():
    """Verify QualityGate catches overloaded metrics and heals them."""
    divisions, all_agents = OrganizationHierarchy.build(agents_per_team=10)
    gate = QualityGate(max_allowed_load=90.0, max_allowed_std=12.0)
    
    test_team = divisions[0].labs[0].teams[0]
    # Inject overload
    for a in test_team.agents:
        a.grid_load_pct = 98.0
        
    m = test_team.evaluate_metrics()
    approved, reason = gate.inspect(m)
    assert not approved
    assert "CRITICAL" in reason
    
    # Heal
    gate.self_heal(test_team)
    m_healed = test_team.evaluate_metrics()
    approved_healed, _ = gate.inspect(m_healed)
    assert approved_healed

def test_v2_adversarial_injection_and_rollback():
    """Verify AdversarialEngine injects disruption and restores 100% state."""
    divisions, all_agents = OrganizationHierarchy.build(agents_per_team=10)
    adv = AdversarialEngine()
    
    sample_agents = all_agents[:50]
    baseline_loads = [a.grid_load_pct for a in sample_agents]
    
    adv.inject_disaster(sample_agents)
    for a in sample_agents:
        assert a.grid_load_pct > 80.0
        
    res = adv.defend_and_recover(sample_agents)
    assert res["recovery_rate_pct"] == 100.0
    
    restored_loads = [a.grid_load_pct for a in sample_agents]
    assert baseline_loads == restored_loads

def test_v2_executive_summarizer(tmp_path):
    """Verify ExecutiveSummarizer outputs valid CSV and JSON with 3 core KPIs."""
    divisions, all_agents = OrganizationHierarchy.build(agents_per_team=10)
    summary = ExecutiveSummarizer.summarize(all_agents, output_dir=str(tmp_path))
    
    assert "executive_kpis" in summary
    assert "action_items" in summary
    assert len(summary["action_items"]) == 5
    assert (tmp_path / "v2_executive_summary.csv").exists()
    assert (tmp_path / "v2_executive_summary.json").exists()
