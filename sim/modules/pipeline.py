import logging
import random
from .agents import create_agent, AgentBase

class Simulation:
    """Simplified simulation orchestrator.
    
    This stub implements the minimal interface required by `simulate.py`.
    It loads the configuration, creates agents according to the specified
    groups, and provides a `run` method that iterates over timesteps while
    invoking each agent's `step` method. Metric computation is delegated to
    the `metrics` module after the run.
    """

    def __init__(self, config):
        self.cfg = config
        self.agents = []
        self.current_minute = 0
        self._setup_logging()
        self._initialize_agents()

    def _setup_logging(self):
        logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
        self.logger = logging.getLogger("Simulation")

    def _initialize_agents(self):
        """Create agents based on the configuration.
        
        The configuration defines a ``groups`` mapping with size and any
        additional parameters required by the specific agent class.
        """
        groups_cfg = self.cfg.get("agents", {}).get("groups", {})
        agent_id = 0
        for group_name, attrs in groups_cfg.items():
            size = attrs.get("size", 0)
            # Remove the ``size`` key before passing the rest as kwargs
            kwargs = {k: v for k, v in attrs.items() if k != "size"}
            for _ in range(size):
                agent = create_agent(agent_id, group_name, **kwargs)
                self.agents.append(agent)
                agent_id += 1
        # Fill the remainder of the total population with generic agents
        total = self.cfg.get("agents", {}).get("total", 0)
        remaining = max(0, total - len(self.agents))
        for _ in range(remaining):
            agent = AgentBase(agent_id, archetype="Generic")
            self.agents.append(agent)
            agent_id += 1
        self.logger.info("Initialized %d agents (including %d new‑group agents).", len(self.agents), len(self.agents) - remaining)

    # ----- Simulation state helpers (stubs) -----
    @property
    def active_ideas(self):
        """Placeholder for the collection of active ideas.
        In a full implementation this would be a list of Idea objects.
        Here we provide a minimal list with dummy objects so that the
        agent behaviours can reference the expected attributes.
        """
        class DummyIdea:
            def __init__(self):
                self.adoption_rate = random.random()
                self.spread_rate = 1.0
                self.quality = random.random()
                self.reach = random.randint(1, 1000)
        # Return a small static list; agents may mutate it.
        if not hasattr(self, "_dummy_ideas"):
            self._dummy_ideas = [DummyIdea() for _ in range(5)]
        return self._dummy_ideas

    def spawn_random_idea(self):
        self.logger.debug("Spawner: Adding a random idea.")
        self.active_ideas.append(self.active_ideas[0])  # simple placeholder

    def combine_ideas(self, i1, i2, boost=1.2):
        # Return a new dummy idea with boosted quality/reach.
        new = type(i1)()
        new.quality = max(i1.quality, i2.quality) * boost
        new.reach = i1.reach + i2.reach
        new.adoption_rate = (i1.adoption_rate + i2.adoption_rate) / 2
        new.spread_rate = (i1.spread_rate + i2.spread_rate) / 2
        return new

    def add_idea(self, idea):
        self.active_ideas.append(idea)

    def current_load(self):
        # Simple proxy: ratio of messages sent to total agents
        total_msgs = sum(a.messages_sent for a in self.agents)
        return total_msgs / (len(self.agents) * 10.0)  # arbitrary scaling

    def apply_quota(self, soft, hard):
        self.logger.info("Regulator: Applying quota soft=%.2f hard=%.2f", soft, hard)
        # In this stub we do not enforce quotas; real logic would limit messages.

    def network_resilience(self):
        return 0.94

    def total_messages_by_group(self, group_name):
        return sum(a.messages_sent for a in self.agents if getattr(a, "archetype", None) == group_name)

    def joint_idea_count(self):
        return len(self.active_ideas)

    def low_quality_ideas(self):
        return sum(1 for i in self.active_ideas if getattr(i, "quality", 1.0) < 0.3)

    def suppressed_ideas(self):
        return sum(1 for i in self.active_ideas if getattr(i, "spread_rate", 1.0) == 0)

    # ----- Run loop -----
    def run(self, run_name="Run1"):
        """Execute the simulation for the configured duration.
        The actual behaviour is heavily simplified – we simply iterate over
        timesteps and call each agent's ``step`` method. Some agents (e.g.,
        ``Explorer``) expect the current minute, so we pass it when the
        method signature matches.
        """
        duration_days = self.cfg.get("simulation", {}).get("duration_days", 30)
        timestep_minutes = self.cfg.get("simulation", {}).get("timestep_minutes", 5)
        total_steps = int((duration_days * 24 * 60) / timestep_minutes)
        self.logger.info("Starting %s for %d steps (%.1f days).", run_name, total_steps, duration_days)
        for step in range(total_steps):
            self.current_minute = step * timestep_minutes
            for agent in self.agents:
                # Call with appropriate signature if the agent expects the minute.
                try:
                    # Inspect the ``step`` function's argument count.
                    if agent.__class__.__name__ == "Explorer":
                        agent.step(self, self.current_minute)
                    else:
                        agent.step(self)
                except Exception as e:
                    self.logger.exception("Agent %s raised an error: %s", agent.id, e)
        self.logger.info("Simulation %s completed.", run_name)
