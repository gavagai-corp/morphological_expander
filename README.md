# Morphological Expansion Tool

A Python wrapper to morphologically expand terms using the [UniMorph](https://unimorph.github.io/) knowledge base. Lemmatizes the input terms and re-inflects the lemma to all possible surface forms.

# How to get started

Clone or download this repository to your own machine. No external libraries are required, so no installation is needed as long as the folder named 'resources' is included. The tool currently works for Swedish, French and Spanish. This may be extended by adding the UniMorph file of the desired language in 'resources'.

# Usage

Runs with Python from the command line. Takes two arguments, the word to be re-inflected and the corresponding language code (ISO 639). If no code is provided, Swedish (sv) is taken as the default.

The functionality can also be used in an interactive python session, by importing the library in the normal way.

## Example

### Input:

$ python3 morphological_expander.py abstraktioner

### Output:

Expanding abstraktioner. No language code provided. Default is Swedish (sv).<br/>
abstraktion<br/>
abstraktions<br/>
abstraktionen<br/>
abstraktioner<br/>
abstraktionens<br/>
abstraktioners<br/>
abstraktionerna<br/>
abstraktionernas<br/>
