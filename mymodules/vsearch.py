def search_for_letters(phrase: str, letters: str) -> set:
    """Display letters found in an asked-for word."""
    return set(letters).intersection(set(phrase))


def search_for_vowels(phrase: str) -> set:
    """Display any vowel found in an asked-for word."""
    return search_for_letters(phrase, 'aeiou')
