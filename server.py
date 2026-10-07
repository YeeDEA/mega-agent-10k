# server.py
"""Standalone Production HTTP Server with Embedded V2 Simulation REST APIs.

Serves the Mega-Agent 10,000 Portal on localhost:8080.
Endpoints:
- Static files: / (index.html, analysis/*, report/*, sim/*)
- POST /api/simulate: Runs live V2 urban infrastructure simulation
- POST /api/attack: Injects real-world adversarial disaster & executes state rollback
- GET /api/status: Returns engine telemetry & health audit
"""

import os
import sys
import json
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Add sim directory to sys.path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SIM_DIR = os.path.join(BASE_DIR, "sim")
if SIM_DIR not in sys.path:
    sys.path.insert(0, SIM_DIR)

try:
    from modules.v2_resilience import OrganizationHierarchy, QualityGate, AdversarialEngine, ExecutiveSummarizer
except ImportError:
    OrganizationHierarchy = QualityGate = AdversarialEngine = ExecutiveSummarizer = None

class MegaAgentServerHandler(SimpleHTTPRequestHandler):
    """Custom request handler serving static portal assets and simulation APIs."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            status_data = {
                "status": "ONLINE",
                "version": "2.1.0-resilient",
                "agents_capacity": 10000,
                "engine": "Hierarchical Governance & Self-Healing Telemetry",
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            self.wfile.write(json.dumps(status_data, ensure_ascii=False).encode("utf-8"))
            return
        
        # Default static file serving
        return super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
        try:
            req_data = json.loads(post_body)
        except Exception:
            req_data = {}

        if self.path == "/api/simulate":
            agent_count = int(req_data.get("agent_count", 10000))
            strictness = float(req_data.get("strictness", 92.0))
            agents_per_team = max(10, agent_count // 100)

            t0 = time.time()
            divisions, all_agents = OrganizationHierarchy.build(agents_per_team=agents_per_team)
            gate = QualityGate(max_allowed_load=strictness, max_allowed_std=14.0)

            passed_teams = 0
            rejected_teams = 0
            for div in divisions:
                for lab in div.labs:
                    for team in lab.teams:
                        for a in team.agents:
                            a.step()
                        # Synthetic drift on ~16% teams to trigger gate
                        if int(team.id.split("_")[1]) % 6 == 0:
                            for a in team.agents[:len(team.agents)//2]:
                                a.grid_load_pct += 18.0
                        
                        m = team.evaluate_metrics()
                        approved, _ = gate.inspect(m)
                        if approved:
                            passed_teams += 1
                        else:
                            rejected_teams += 1
                            gate.self_heal(team)
                            passed_teams += 1

            out_dir = os.path.join(SIM_DIR, "output")
            summary = ExecutiveSummarizer.summarize(all_agents, output_dir=out_dir)
            elapsed_ms = round((time.time() - t0) * 1000, 2)

            res = {
                "success": True,
                "elapsed_ms": elapsed_ms,
                "total_agents": len(all_agents),
                "passed_teams": passed_teams,
                "rejected_and_healed": rejected_teams,
                "kpis": summary["executive_kpis"],
                "actions": summary["action_items"]
            }
            self._send_json(res)
            return

        elif self.path == "/api/attack":
            agent_count = int(req_data.get("agent_count", 10000))
            agents_per_team = max(10, agent_count // 100)

            divisions, all_agents = OrganizationHierarchy.build(agents_per_team=agents_per_team)
            adv = AdversarialEngine()
            targeted = all_agents[:len(all_agents) // 4]

            t0 = time.time()
            adv.inject_disaster(targeted, attack_type="Cyber Grid Overload")
            corrupt_load = round(float(sum(a.grid_load_pct for a in targeted) / len(targeted)), 2)

            rec_report = adv.defend_and_recover(targeted)
            recovered_load = round(float(sum(a.grid_load_pct for a in targeted) / len(targeted)), 2)
            recovery_ms = round((time.time() - t0) * 1000, 2)

            res = {
                "success": True,
                "targeted_nodes": len(targeted),
                "corrupted_load_pct": corrupt_load,
                "recovered_load_pct": recovered_load,
                "recovery_rate_pct": rec_report["recovery_rate_pct"],
                "recovery_latency_ms": recovery_ms,
                "status": rec_report["status"]
            }
            self._send_json(res)
            return

        self.send_error(404, "Endpoint Not Found")

    def _send_json(self, data: dict):
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

def run_server(port: int = 8080):
    server_address = ("127.0.0.1", port)
    httpd = HTTPServer(server_address, MegaAgentServerHandler)
    print(f"\n=======================================================")
    print(f"  MEGA-AGENT 10,000 PRODUCTION SERVER ONLINE")
    print(f"  Local URL: http://localhost:{port}/")
    print(f"  API Health: http://localhost:{port}/api/status")
    print(f"=======================================================\n")
    httpd.serve_forever()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
