from base4 import Sentence, Text

class Program:
    @staticmethod
    def main():
        sentences_list = [
            Sentence("Stone is a solid block.", "Stone", "Structural", 1.5, 6.0, False),
            Sentence("Dirt breaks very easily.", "Dirt", "Natural", 0.5, 0.5, False),
            Sentence("Obsidian withstands TNT.", "Obsidian", "Natural", 50.0, 1200.0, False),
            Sentence("Glass is transparent.", "Glass", "Ornamental", 0.3, 0.3, True),
            Sentence("Heavy stone variant.", "Heavy Stone", "Structural", 1.5, 10.0, False)
        ]

        text_container = Text(sentences_list)
        sentences = text_container.get_sentences()

        print("Оригінальний порядок:")
        for s in sentences:
            print(s)

        sorted_sentences = sorted(sentences, key=lambda s: (s.hardness, -s.blast_resistance))
        print("\nВідсортований порядок (За зростанням по hardness, За спаданням по Blast resistance):")
        for s in sorted_sentences:
            print(s)

        target = Sentence("Glass is transparent.", "Glass", "Ornamental", 0.3, 0.3, True)
        print("\nРезультат пошуку:")
        found_sentence = next((s for s in sorted_sentences if s == target), None)
        if found_sentence:
            print(f"Знайдено: {found_sentence}")
        else:
            print("Не знайдено")

        dirty_text = "Текст   з \t\t багатьма    пробілами."
        cleaned = Text.clean_string(dirty_text)
        print(f"\nВидалено зайві пробіли: {cleaned}")

if __name__ == "__main__":
    Program.main()
