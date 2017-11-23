# Morphological Expansion Tool

A Python wrapper to mophologically expand terms using the UniMorph knowledge base. Lemmatises the input terms and re-inflects the lemma to all possible surface forms.

# Usage

Runs with Python from the command line. Takes two arguments, the word to re-inflect and the corresponding language code (ISO 639). If no code is provided, Swedish (sv) is taken as the default.

## Example

### Input:

$ python3 morphological_expander.py abstraktioner

### Output:

Expanding abstraktioner. No language code provided. Default is Swedish (sv).
abstraktion
abstraktions
abstraktionen
abstraktioner
abstraktionens
abstraktioners
abstraktionerna
abstraktionernas
