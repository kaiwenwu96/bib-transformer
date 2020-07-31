import sys
sys.path.append('biblib')

import time
import unicodedata

import biblib.bib
import biblib.messages
import biblib.algo

import argparse


def get_id(ent):
    authors = [biblib.algo.tex_to_unicode(author.pretty(), pos=ent.field_pos['author']) for author in ent.authors()]
    # authors = [biblib.algo.tex_to_ascii(author.pretty(), pos=ent.field_pos['author']) for author in ent.authors()]
    authors = [unicodedata.normalize('NFKD', author).encode('ascii', 'ignore').decode("utf-8") for author in authors]

    ret = ""

    if len(authors) == 1:
        ret += authors[0].split(' ')[-1]
    elif len(authors) == 2:
        ret += authors[0].split(' ')[-1] + authors[1].split(' ')[-1]
    elif len(authors) >= 3:
        ret += authors[0].split(' ')[-1]
        ret += "".join([authors[i].split(' ')[-1][0] for i in range(1, len(authors))])
    else:
        raise Exception()

    ret += "{:02d}".format(int(ent['year']) % 100)

    return ret


def change_id(ent):
    ent.key = get_id(ent)
    return ent


def insert_url(ent):
    if 'url' in ent:
        ent['title'] = "\\href{{{}}}{{{}}}".format(ent['url'], ent['title'])

    return ent


def get_conference(ent):
    entry = ""
    entry += "@{}{{{},\n".format(ent.typ, ent.key)
    entry += "  title     = {{{}}},\n".format(ent['title'])
    entry += "  author    = {{{}}},\n".format(ent['author'])
    entry += "  booktitle = {{{}}},\n".format(ent['booktitle'])
    if 'pages' in ent:
        entry += "  pages     = {{{}}},\n".format(ent['pages'])
    entry += "  year      = {{{}}},\n".format(ent['year'])
    entry += "}"
    return entry


def get_journal(ent):
    entry = ""
    entry += "@{}{{{},\n".format(ent.typ, ent.key)
    entry += "  title   = {{{}}},\n".format(ent['title'])
    entry += "  author  = {{{}}},\n".format(ent['author'])
    entry += "  journal = {{{}}},\n".format(ent['journal'])
    entry += "  volume  = {{{}}},\n".format(ent['volume'])
    entry += "  pages   = {{{}}},\n".format(ent['pages'])
    entry += "  year    = {{{}}},\n".format(ent['year'])
    entry += "}"
    return entry


def get_preprint(ent):
    entry = ""
    entry += "@{}{{{},\n".format(ent.typ, ent.key)
    entry += "  title  = {{{}}},\n".format(ent['title'])
    entry += "  author = {{{}}},\n".format(ent['author'])
    entry += "  note   = {{{}}},\n".format(ent['note'])
    entry += "  year   = {{{}}},\n".format(ent['year'])
    entry += "}"
    return entry


def get_book(ent):
    entry = ""
    entry += "@{}{{{},\n".format(ent.typ, ent.key)
    entry += "  title     = {{{}}},\n".format(ent['title'])
    entry += "  author    = {{{}}},\n".format(ent['author'])
    entry += "  publisher = {{{}}},\n".format(ent['publisher'])
    # entry += "  edition   = {{{}}},\n".format(ent['edition'])
    entry += "  year      = {{{}}},\n".format(ent['year'])
    entry += "}"
    return entry


def get_misc(ent):
    entry = ""
    entry += ""
    entry += "@{}{{{},\n".format(ent.typ, ent.key)
    entry += "  title     = {{{}}},\n".format(ent['title'])
    entry += "  author    = {{{}}},\n".format(ent['author'])
    entry += "  year      = {{{}}},\n".format(ent['year'])
    entry += "}"
    return entry


def ent2bib(ent):
    if ent.typ in ['inproceedings', 'incollection', 'InProceedings']:
        ent.typ = 'inproceedings'
        s = get_conference(ent)
    elif ent.typ == 'article':
        s = get_journal(ent)
    elif ent.typ in ['preprint', 'unpublished']:
        ent.typ = 'unpublished'
        s = get_preprint(ent)
    elif ent.typ == 'book':
        s = get_book(ent)
    elif ent.typ == 'misc':
        s = get_misc(ent)
    else:
        raise Exception("Unknown bib entry type")

    return s


def ent2latex(ent):
    def get_venue(ent):
        if ent.typ in ['inproceedings', 'incollection', 'InProceedings']:
            return ent['booktitle']
        elif ent.typ == 'article':
            return ent['journal']
        elif ent.typ == 'preprint':
            return ent['note']
        else:
            raise Exception("cannot handle")

    entry = ""
    authors = [biblib.algo.tex_to_unicode(author.pretty(), pos=ent.field_pos['author']) for author in ent.authors()]
    entry += ", ".join([author if author != "Kaiwen Wu" else "\\textbf{Kaiwen Wu}" for author in authors]) + " \\\\\n"
    entry += ent['title'] + " \\\\\n"
    entry += get_venue(ent) + ", "
    entry += ent['year'] + " \\\\\n"

    return entry


def ent2html(ent):
    assert 0


def transform(in_file, out_file, option):
    bib = open(in_file, "r")

    # Load databases
    db = biblib.bib.Parser().parse(bib, log_fp=sys.stderr).get_entries()

    # Resolve cross-references
    db = biblib.bib.resolve_crossrefs(db)

    # Print entries
    recoverer = biblib.messages.InputErrorRecoverer()

    ent_lst = [ent for ent in db.values()]

    for ent in ent_lst:
        ent = change_id(ent)

    id_lst = [xx.key for xx in ent_lst]
    new_id_lst = []

    for ent in ent_lst:
        if len([xx for xx in id_lst if xx == ent.key]) == 1:
            new_id_lst.append(ent.key)
        else:
            for ch in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
                if ent.key + ch not in new_id_lst:
                    ent.key += ch
                    break
            new_id_lst.append(ent.key)

    def key_func(ent):
        authors = [biblib.algo.tex_to_unicode(author.pretty(), pos=ent.field_pos['author']) for author in ent.authors()]
        authors = [unicodedata.normalize('NFKD', author).encode('ascii', 'ignore').decode("utf-8") for author in authors]

        return str.lower(authors[0].split(' ')[-1])

    ent_lst.sort(key=key_func)

    for ent in ent_lst:
        ent = insert_url(ent)

        if option == "bib":
            s = ent2bib(ent)
        elif option == "latex":
            s = ent2latex(ent)
        elif option == "html":
            s = ent2html(ent)

        print("{}\n".format(s))

    recoverer.reraise()

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--in_file', type=str, default=None, help='.bib file to process')
    arg_parser.add_argument('--out_file', type=str, default=None, help='str or None. File to dump results. None indicates standard output.')
    arg_parser.add_argument('--option', type=str, default="bib", help='bib | latex | html')
    arg_parser.add_argument('--loop', type=int, default=0, help='Whether to recursively run the procedure. Default: 0')

    args = arg_parser.parse_args()


    try:
        while True:
            if args.out_file is not None:
                sys.stdout = open(args.out_file, 'w')

            transform(args.in_file, args.out_file, args.option)

            if args.out_file is not None:
                sys.stdout.close()

            if not args.loop:
                break

            time.sleep(30)


    except biblib.messages.InputError:
        sys.exit(1)
