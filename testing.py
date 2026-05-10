from base4 import Word, Punctuation, Sentence, Text

def test_initialization():
    word = Word("Block")
    assert len(word.letters) == 5
    assert word.content == "Block"

    sentence = Sentence("Hello, world", "TestBlock", "TestCat", 1.0, 1.0, False)
    assert len(sentence.elements) == 3
    assert isinstance(sentence.elements[0], Word)
    assert sentence.elements[0].content == "Hello"
    assert isinstance(sentence.elements[1], Punctuation)
    assert sentence.elements[1].mark == ","
    assert isinstance(sentence.elements[2], Word)
    assert sentence.elements[2].content == "world"

def test_equals_and_tostring():
    s1 = Sentence("Some text", "Stone", "Structural", 1.5, 6.0, False)
    s2 = Sentence("Some text", "Stone", "Structural", 1.5, 6.0, False)
    s3 = Sentence("Some text", "Dirt", "Natural", 0.5, 0.5, False)
    assert s1 == s2
    assert s1 != s3

def test_eq():
    s1 = Sentence("Some text", "Stone", "Structural", 1.5, 6.0, False)
    #{self.name} -> Category: {self.category}; Hardness: {str(self.hardness)}; BlastResist: {self.blast_resistance}
    expected_str = "Stone -> Category: Structural; Hardness: 1.5; BlastResist: 6.0"
    assert str(s1) == expected_str


def test_sorting_logic():
    s1 = Sentence("T1", "A", "Cat", 2.0, 5.0, False)
    s2 = Sentence("T2", "B", "Cat", 1.0, 1.0, False)
    s3 = Sentence("T3", "C", "Cat", 2.0, 10.0, False)
    sentences = [s1, s2, s3]
    sentences = sorted(sentences, key=lambda s: (s.hardness, -s.blast_resistance))
    # очікуваний порядок:
        # 1. "s2" (Hardness 1.0)
        # 2. "s3" (Hardness 2.0, BlastRes 10.0)
        # 3. "s1" (Hardness 2.0, BlastRes 5.0)
    assert sentences == [s2, s3, s1]
    
def test_clean_string():
    dirty_text = "   Багато \t\t зайвих    пробілів   "
    expected_text = "Багато зайвих пробілів"
    text_obj = Text([])
    assert text_obj.clean_string(dirty_text) == expected_text
