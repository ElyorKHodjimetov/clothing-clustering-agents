# coordinator.py

import networkx as nx
from collections import defaultdict

class CoordinatorAgent:
    """
    Координатор, который собирает голоса от экспертов–агентов
    и формирует итоговые кластеры как связные компоненты графа.
    """
    def __init__(self, threshold: int):
        self.threshold = threshold

    def combine_votes(self, votes_list, items):
        # Суммируем голоса по каждой паре
        total = defaultdict(int)
        for votes in votes_list:
            for pair, v in votes.items():
                total[pair] += v

        # Строим граф схожести
        G = nx.Graph()
        G.add_nodes_from([item.id for item in items])
        for (i, j), cnt in total.items():
            if cnt >= self.threshold:
                G.add_edge(i, j)

        # Извлекаем кластеры как связные компоненты
        clusters = []
        for comp in nx.connected_components(G):
            clusters.append([item for item in items if item.id in comp])
        return clusters
