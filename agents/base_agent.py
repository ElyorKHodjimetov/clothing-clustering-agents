class BaseAgent:
    """
    Базовый класс для агентов.
    Метод vote_pairs должен возвращать словарь { (id_i, id_j): 0 или 1 }.
    """
    def vote_pairs(self, items):
        raise NotImplementedError