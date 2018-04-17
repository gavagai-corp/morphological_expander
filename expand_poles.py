import os
from morphological_expander import get_related_morphological_forms


def inflect_pole(pole_file, pole_language_code):
    """Takes a txt filepath, finds any new inflections from the resource and saves a new file with these added.
    Any existing duplicates are removed in passing."""
    existing_pole_terms = []

    with open(pole_file,mode='r',encoding='utf8') as f:
        for line in f:
            existing_pole_terms.append(line.strip())

    print('Pole:', pole_file)
    print(existing_pole_terms)
    len_existing_pole_terms = len(existing_pole_terms)
    print('{} terms in pole initially.'.format(len_existing_pole_terms))

    retrieved_expansions = []
    failed_terms = []
    count = 0

    for term in existing_pole_terms:

        try:
            reinflections = get_related_morphological_forms(term, pole_language_code)
            if len(reinflections) > 0:
                retrieved_expansions += reinflections
        except:
            failed_terms.append(term)
            term += ' FAIL'

        count += 1
        print('Prog:', round(100 * count / len_existing_pole_terms, 2), term)

    terms_to_add = list(set(retrieved_expansions))

    new_expanded_pole = sorted(list(set(existing_pole_terms + terms_to_add)))

    print('{} terms in pole after reinflection.'.format(len(new_expanded_pole)))
    print(new_expanded_pole)
    print(failed_terms)

    with open(pole_file[:-4] + '_exp.txt', mode='w', encoding='utf8') as f:
        for term in new_expanded_pole:
            f.write(term + '\n')


def inflect_multiple_poles(directory):
    for file in os.listdir(directory):
        inflect_pole(directory + '/' + file, directory[-2:])


def count_lines_in_file(filename):
    return sum(1 for line in open(filename) if (len(line.strip()) > 0))


def directory_stats(directory):
    files = os.listdir(directory)
    print('\n\t\t\t\t', 'Before', '\t', 'After', '\t\t', 'Diff')
    for polefile in files:
        expanded_pole = polefile[:-4] + '_exp.txt'
        if expanded_pole in files:
            before = count_lines_in_file(directory + '/' + polefile)
            after = count_lines_in_file(directory + '/' + expanded_pole)
            print(polefile, '\n\t\t\t\t', before, '\t\t', after, '\t\t', after - before, '\n')
