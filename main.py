# main.py

import json
from clothing_item import ClothingItem
from agents.color_agent import ColorAgent
from agents.thickness_agent import ThicknessAgent
from agents.sleeve_agent import SleeveAgent
from agents.type_agent import TypeAgent
from coordinator import CoordinatorAgent

def load_items(path):
    with open(path, encoding='utf-8') as f:
        return [ClothingItem(d) for d in json.load(f)]

if __name__ == '__main__':
    items = load_items('data/clothing_items.json')
    agents = [ColorAgent(), ThicknessAgent(), SleeveAgent(), TypeAgent()]
    votes_list = [ag.vote_pairs(items) for ag in agents]
    coord = CoordinatorAgent(threshold=2)
    clusters = coord.combine_votes(votes_list, items)
    for idx, cluster in enumerate(clusters, 1):
        print(f"Cluster {idx}: {[it.id for it in cluster]}")
