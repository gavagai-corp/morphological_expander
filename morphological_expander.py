import re
import sys


def lemmatize(surface_form, language_code):
    with open('resources/' + language_code + '.txt', encoding='utf8') as f:
        for line in f:
            if re.search(r'\t' + surface_form + '\t', line):
                lemma = line.split('\t')[0]  # Each line contains: lemma surface_form details
                return lemma
        return 'Not in resource.'


def expand_lemma_to_surface_forms(lemma_to_expand, language_code):
    surface_forms = []

    with open('resources/' + language_code + '.txt', encoding='utf8') as f:
        for line in f:
            current_lemma, surface_form, _ = line.split('\t')
            if current_lemma == lemma_to_expand:
                surface_forms.append(surface_form)

    if len(surface_forms) > 1:
        return set(surface_forms)
    else:
        return 'Not in resource.'


def get_related_morphological_forms(word_to_reinflect, language_code='sv'):
    lemma = lemmatize(word_to_reinflect, language_code)
    expanded_forms = expand_lemma_to_surface_forms(lemma, language_code)
    return expanded_forms


if __name__ == '__main__':
    input_word = sys.argv[1]
    try:
        language_code = sys.argv[2]
        print('Expanding {0}. Language code is {1}.'.format(input_word, language_code))
        output = get_related_morphological_forms(input_word, language_code)
    except IndexError:
        print('Expanding {0}. No language code provided. Default is Swedish (sv).'.format(input_word))
        output = get_related_morphological_forms(input_word)
    for item in sorted(output, key=lambda x: len(x)):
        print(item)
