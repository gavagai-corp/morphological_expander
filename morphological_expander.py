import re


def lemmatize(surface_form, language):
    with open('resources/' + language + '.txt') as f:
        for line in f:
            if re.match(surface_form, line):
                lemma = line.split()[0]  # Each line contains: lemma surface_form details
                return lemma


lemmatise('katter', 'sv')