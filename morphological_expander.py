import re


def lemmatize(surface_form, language):
    with open('resources/' + language + '.txt', encoding='utf8') as f:
        for line in f:
            if re.search(r'\t'+surface_form+'\t', line):
                lemma = line.split('\t')[0]  # Each line contains: lemma surface_form details
                return lemma
        return 'Not in resource'


print(lemmatize('abstraktionernas', 'sv'))