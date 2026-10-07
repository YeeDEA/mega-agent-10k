import random
import logging

class AgentBase:
    def __init__(self, agent_id, archetype):
        self.id = agent_id
        self.archetype = archetype
        self.messages_sent = 0
        self.quality_score = random.random()

    def step(self, sim_state):
        """Perform a simulation step. Base agents do nothing special."""
        pass

# New group behaviours
class Catalyst(AgentBase):
    def __init__(self, agent_id, amplification_factor=1.5):
        super().__init__(agent_id, "Catalyst")
        self.amplification_factor = amplification_factor

    def step(self, sim_state):
        # Boost high‑impact ideas
        for idea in sim_state.active_ideas:
            if idea.adoption_rate > 0.3:
                idea.spread_rate *= self.amplification_factor
        self.messages_sent += 1

class Guardian(AgentBase):
    def __init__(self, agent_id, suppression_threshold=0.2):
        super().__init__(agent_id, "Guardian")
        self.suppression_threshold = suppression_threshold

    def step(self, sim_state):
        for idea in sim_state.active_ideas:
            if idea.quality < self.suppression_threshold:
                idea.spread_rate = 0  # suppress
        self.messages_sent += 1

class Explorer(AgentBase):
    def __init__(self, agent_id, seed_interval_hours=12):
        super().__init__(agent_id, "Explorer")
        self.seed_interval = seed_interval_hours * 60  # minutes
        self.last_seed = -self.seed_interval

    def step(self, sim_state, current_minute):
        if current_minute - self.last_seed >= self.seed_interval:
            sim_state.spawn_random_idea()
            self.last_seed = current_minute
        self.messages_sent += 1

class Collaborator(AgentBase):
    def __init__(self, agent_id):
        super().__init__(agent_id, "Collaborator")
        self.team = []

    def step(self, sim_state):
        # Simple co‑creation: combine two random ideas
        if len(sim_state.active_ideas) >= 2:
            i1, i2 = random.sample(sim_state.active_ideas, 2)
            new_idea = sim_state.combine_ideas(i1, i2, boost=1.2)
            sim_state.add_idea(new_idea)
        self.messages_sent += 1

class Regulator(AgentBase):
    def __init__(self, agent_id, load_threshold=0.7, quota_soft=0.9, quota_hard=0.8):
        super().__init__(agent_id, "Regulator")
        self.load_threshold = load_threshold
        self.quota_soft = quota_soft
        self.quota_hard = quota_hard

    def step(self, sim_state):
        load = sim_state.current_load()
        if load > self.load_threshold:
            sim_state.apply_quota(self.quota_soft, self.quota_hard)
        self.messages_sent += 1

# Factory to create appropriate agent type based on group
def create_agent(agent_id, group_name, **kwargs):
    if group_name == "Catalysts":
        return Catalyst(agent_id, **kwargs)
    if group_name == "Guardians":
        return Guardian(agent_id, **kwargs)
    if group_name == "Explorers":
        return Explorer(agent_id, **kwargs)
    if group_name == "Collaborators":
        return Collaborator(agent_id)
    if group_name == "Regulators":
        return Regulator(agent_id, **kwargs)
    # Default base agent for other archetypes
    return AgentBase(agent_id, archetype=group_name)
