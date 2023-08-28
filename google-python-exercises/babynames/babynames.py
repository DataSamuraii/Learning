import sys
import re


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    with open(filename, 'r') as file:
        content = file.read()

        year_match = re.search(r'Popularity in (\d{4})', content)
        if not year_match:
            return

        year = year_match.group(1)
        names_list = [year]
        
        names_matches = re.findall(r'<td>(\d+)<\/td><td>(\w+)<\/td><td>(\w+)<\/td>', content)
        names_dict = {name: rank for rank, name1, name2 in names_matches for name in (name1, name2)}

        names_list.extend([f'{name} {rank}' for name, rank in sorted(names_dict.items())])

    return names_list


def main():
    if len(sys.argv) < 2:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    summary = '--summaryfile' in sys.argv
    if summary:
        sys.argv.remove('--summaryfile')

    for filename in sys.argv[1:]:
        names = extract_names(filename)
        if summary:
            with open(filename + '.summary', 'w') as f:
                f.write('\n'.join(names))
        else:
            print('\n'.join(names))


if __name__ == '__main__':
    main()
