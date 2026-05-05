import re

class Letter:
    def __init__(self, char: str):
        self.char = char

    def __str__(self) -> str:
        return self.char

class Word:
    def __init__(self, word_text: str):
        self.letters = [Letter(c) for c in word_text]
        self.content = word_text

    def __str__(self) -> str:
        return self.content

class Punctuation:
    def __init__(self, mark: str):
        self.mark = mark

    def __str__(self) -> str:
        return self.mark

class Sentence:
    def __init__(self, sentence_text: str, name: str, category: str, hardness: float, blast_resistance: float, is_transparent: bool):
        self.elements = []
        tokens = re.findall(r"\w+|[^\w\s]", sentence_text)
        for token in tokens:
            if token.isalnum():
                self.elements.append(Word(token))
            else:
                self.elements.append(Punctuation(token))

        self.name = name
        self.category = category
        self.hardness = hardness
        self.blast_resistance = blast_resistance
        self.is_transparent = is_transparent

    def __str__(self) -> str:
        return f"{self.name} -> Category: {self.category}; Hardness: {str(self.hardness)}; BlastResist: {self.blast_resistance}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Sentence):
            return False
        return (self.name == other.name and
                self.category == other.category and
                self.hardness == other.hardness and
                self.blast_resistance == other.blast_resistance and
                self.is_transparent == other.is_transparent)

class Text:
    def __init__(self, sentences: list):
        self._sentences = sentences

    def get_sentences(self) -> list:
        return self._sentences

    def clean_string(self, raw_string: str) -> str:
        return re.sub(r'[ \t]+', ' ', raw_string).strip()
