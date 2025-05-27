# clothing_item.py

class ClothingItem:
    def __init__(self, data: dict):
        self.id = data.get("id")
        self.color = data.get("цвет")
        self.thickness = data.get("толщина")
        self.sleeve = data.get("рукав")
        self.type = data.get("тип")
        self.category = None

    def __repr__(self):
        return (f"<ClothingItem id={self.id} "
                f"color={self.color!r} "
                f"thickness={self.thickness!r} "
                f"sleeve={self.sleeve!r} "
                f"type={self.type!r}>")
