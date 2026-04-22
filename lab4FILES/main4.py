from base4 import BuildingBlock, BlockIdentity, Physics, Visuals

class LabExecutor:
    @staticmethod
    def run():
        blocks = [
            BuildingBlock(BlockIdentity("Stone", "Structural"), Physics(1.5, 6.0), Visuals(False)),
            BuildingBlock(BlockIdentity("Dirt", "Natural"), Physics(0.5, 0.5), Visuals(False)),
            BuildingBlock(BlockIdentity("Glass", "Ornamental"), Physics(0.3, 0.3), Visuals(True)),
            BuildingBlock(BlockIdentity("Obsidian", "Natural"), Physics(50.0, 1200.0), Visuals(False)),
            # додаю ще один камінь для перевірки складного сортування
            BuildingBlock(BlockIdentity("Heavy Stone", "Structural"), Physics(1.5, 10.0), Visuals(False))  ]

        print("Оригінальний масив:")
        for b in blocks:
            print(b)

        # сортування: hardness (за зростання), blast_resistance (за спадання)
        blocks.sort(key=lambda b: (b.physics.hardness, -b.physics.blast_resistance))

        print("\nВідсортований масив:")
        for b in blocks:
            print(b)

        # пошук ідентичного блоку
        target = BuildingBlock(BlockIdentity("Glass", "Ornamental"), Physics(0.3, 0.3), Visuals(True))

        print(f"\nШукаємо: {target}")
        if target in blocks:
            index = blocks.index(target)
            print(f"Успіх! Ідентичний блок знайдено за номером: {index+1}")
        else:
            print("Блок не знайдено.")

if __name__ == "__main__":
    LabExecutor.run()
