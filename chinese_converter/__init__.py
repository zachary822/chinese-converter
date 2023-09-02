import json
from collections import Counter, defaultdict, deque
from importlib import resources
from operator import itemgetter
from typing import Any

__all__ = ["to_simplified", "to_traditional"]

PKG = resources.files("chinese_converter")

with resources.as_file(PKG / "traditional.txt") as p, p.open(encoding="utf-8") as f, resources.as_file(
    PKG / "simplified.txt"
) as q, q.open(encoding="utf-8") as g:
    traditional, simplified = f.read().strip(), g.read().strip()

with resources.as_file(PKG / "bigram.json") as p, p.open(encoding="utf-8") as f, resources.as_file(
    PKG / "monogram.json"
) as q, q.open(encoding="utf-8") as g:
    bigrams, monograms = Counter(json.load(f)), Counter(json.load(g))

simp_to_trad: dict[str, list[str]] = defaultdict(list)
trad_to_simp = str.maketrans(traditional, simplified)

for s, t in zip(simplified, traditional):
    simp_to_trad[s].append(t)

simp_to_trad = dict(simp_to_trad)


def default_getter(lst, i, default: Any | None = None):
    try:
        return lst[i]
    except IndexError:
        return default


def most_common_word(choices: list[str], prev_word: str | None = None, next_word: str | None = None) -> str:
    bigram_freqs: deque[tuple[str, int]] = deque()

    if prev_word is not None:
        bigram_freqs.extend((c, bigrams[prev_word + c]) for c in choices)

    if next_word is not None:
        bigram_freqs.extend((c, bigrams[c + next_word]) for c in choices)

    try:
        choices_max = max(bigram_freqs, key=itemgetter(1))

        if not choices_max[1]:
            return max(choices, key=lambda c: monograms[c])

        return choices_max[0]
    except ValueError:
        return choices[0]


def to_traditional(text: str) -> str:
    """
    Translates text to traditional chinese

    :param text:
    :return:
    """
    result: deque[str] = deque()

    for i, s in enumerate(text):
        try:
            choices = simp_to_trad[s]

            if len(choices) > 1:
                result.append(most_common_word(choices, default_getter(result, -1), default_getter(text, i + 1)))
            else:
                result.append(choices[0])
        except KeyError:
            result.append(s)

    return "".join(result)


def to_simplified(text: str) -> str:
    """
    Translates text to simplified chinese

    :param text:
    :return:
    """
    return text.translate(trad_to_simp)
