from chinese_converter import to_simplified, to_traditional


class TestTranslator:
    def test_to_simplified(self):
        result = to_simplified("皇后與國王在後面共同候車吃麵")

        assert result == "皇后与国王在后面共同候车吃面"

    def test_to_traditional(self):
        result = to_traditional("皇后与国王在后面共同候车面食后")

        assert result == "皇后與國王在後面共同候車麵食後"

    def test_two_way(self):
        trad = "皇后與國王在後面共同候車"
        result = to_traditional(to_simplified(trad))

        assert trad == result

        simp = "皇后与国王在后面共同候车后"
        result = to_simplified(to_traditional(simp))

        assert simp == result

    def test_other_language(self):
        text = "this is a book."

        assert text == to_simplified(text)
        assert text == to_traditional(text)
