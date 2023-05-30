from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class WordsCountSchema(BaseModel):
    words: List[str]


class WordsSortSchema(WordsCountSchema):
    order: str = None


def count_vowels(word):
    return sum([1 for char in word if char in "aeiou"])


@router.post("/vowel_count")
async def vowel_count(words: WordsCountSchema):
    return {word: count_vowels(word) for word in words.words}


@router.post("/sort")
async def sort_words(words: WordsSortSchema):
    if words.order == "desc":
        return sorted(words.words, reverse=True)
    else:
        return sorted(words.words)
