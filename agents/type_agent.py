from agents.base_agent import BaseAgent

class TypeAgent(BaseAgent):
    def vote_pairs(self, items):
        votes = {}
        for i, a in enumerate(items):
            for j, b in enumerate(items[i+1:], start=i+1):
                votes[(a.id, b.id)] = int(a.type == b.type)
        return votes
