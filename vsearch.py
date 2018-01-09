def search_for_vowels(phrase:str) -> set:
    """Display any vowel found in an asked-for word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
