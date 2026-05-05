from base4 import BlockIdentity, Physics, Visuals, BuildingBlock

def test_block_identity_equality():
    id1 = BlockIdentity("Stone", "Structural")
    id2 = BlockIdentity("Stone", "Structural")
    id3 = BlockIdentity("Dirt", "Natural")
    assert id1 == id2
    assert id1 != id3 
    assert id1 != "Stone" 

def test_physics_equality():
    p1 = Physics(1.5, 6.0)
    p2 = Physics(1.5, 6.0)
    p3 = Physics(50.0, 1200.0)
    assert p1 == p2
    assert p1 != p3

def test_visuals_equality():
    v1 = Visuals(False)
    v2 = Visuals(False)
    v3 = Visuals(True)
    assert v1 == v2
    assert v1 != v3

def test_building_block_composition():
    block1 = BuildingBlock(BlockIdentity("Glass", "Ornamental"),Physics(0.3, 0.3),Visuals(True))
    block2 = BuildingBlock(BlockIdentity("Glass", "Ornamental"),Physics(0.3, 0.3),Visuals(True))
    block3 = BuildingBlock(BlockIdentity("Stone", "Structural"),Physics(1.5, 6.0),Visuals(False))
    assert block1 == block2
    assert block1 != block3
    assert repr(block1) == "Block(name='Glass', hardness=0.3, blast_resistance=0.3)" # перевірка форматування тексту

def test_sorting_logic():
    b1 = BuildingBlock(BlockIdentity("Stone", "A"), Physics(2.0, 5.0), Visuals(False))
    b2 = BuildingBlock(BlockIdentity("Dirt", "B"), Physics(1.0, 1.0), Visuals(False))
    b3 = BuildingBlock(BlockIdentity("Heavy Stone", "C"), Physics(2.0, 10.0), Visuals(False))
    blocks = [b1, b2, b3]
    blocks.sort(key=lambda b: (b.physics.hardness, -b.physics.blast_resistance)) 
    # очікуваний порядок:
    # 1) Dirt (найменший hardness: 1.0)
    # 2) Heavy Stone (однаковий hardness 2.0, але більший blast_resistance 10.0)
    # 3) Stone (однаковий hardness 2.0, але менший blast_resistance 5.0)
    assert blocks[0].identity.name == "Dirt"
    assert blocks[1].identity.name == "Heavy Stone"
    assert blocks[2].identity.name == "Stone"
