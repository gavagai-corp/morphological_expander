import re
import sys


def lemmatize(surface_form, language_code):
    with open('resources/' + language_code + '.txt', encoding='utf8') as f:
        for line in f:
            if re.search(r'\t' + surface_form + '\t', line):
                lemma = line.split('\t')[0]  # Each line contains: lemma \t surface_form \t meta-info
                return lemma


def expand_lemma_to_surface_forms(lemma_to_expand, language_code):
    surface_forms = []

    with open('resources/' + language_code + '.txt', encoding='utf8') as f:
        for line in f:
            current_lemma, surface_form, _ = line.split('\t')
            if current_lemma == lemma_to_expand:
                surface_forms.append(surface_form)
    return set(surface_forms)


def get_related_morphological_forms(word_to_reinflect, language_code='sv'):
    lemma = lemmatize(word_to_reinflect, language_code)
    expanded_forms = expand_lemma_to_surface_forms(lemma, language_code)
    return sorted(expanded_forms, key=lambda x: len(x)) # I admit sorting by length is a little meaningless.


def pretty_print(results):
    if len(results) > 0:
        for item in results:
            print(str(item))
    else:
        print('Not in resource.')


if __name__ == '__main__':
    input_word = sys.argv[1]
    try:
        language_code = sys.argv[2]
        print('Expanding {0}. Language code is {1}.'.format(input_word, language_code))
        output = get_related_morphological_forms(input_word, language_code)
    except IndexError:
        print('Expanding {0}. No language code provided. Default is Swedish (sv).'.format(input_word))
        output = get_related_morphological_forms(input_word)
    pretty_print(output)
