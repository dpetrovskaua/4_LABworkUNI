class BlockIdentity: # ідентифікація блоку (name + category)
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BlockIdentity):
            return NotImplemented
        return self.name == other.name and self.category == other.category

class Physics: # фізичні властивості (hardness + blast_resistance)
    def __init__(self, hardness: float, blast_resistance: float):
        self.hardness = hardness
        self.blast_resistance = blast_resistance

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Physics):
            return NotImplemented
        return self.hardness == other.hardness and self.blast_resistance == other.blast_resistance

class Visuals: # візуальна властивість (is_transparent)
    def __init__(self, is_transparent: bool):
        self.is_transparent = is_transparent

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Visuals):
            return NotImplemented
        return self.is_transparent == other.is_transparent

class BuildingBlock: # всі минулі класи
    def __init__(self, identity: BlockIdentity, physics: Physics, visuals: Visuals):
        self.identity = identity
        self.physics = physics
        self.visuals = visuals

    def __repr__(self) -> str:
        return (f"Block(name='{self.identity.name}', "
                f"hardness={self.physics.hardness}, "
                f"blast_resistance={self.physics.blast_resistance})")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BuildingBlock):
            return NotImplemented
        # порівняння
        return (self.identity == other.identity and
                self.physics == other.physics and
                self.visuals == other.visuals)
