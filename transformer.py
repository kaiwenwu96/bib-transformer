import sys
sys.path.append('biblib')

import biblib.bib
import biblib.messages
import biblib.algo
import argparse


def get_id(ent):
    # authors = [biblib.algo.tex_to_unicode(author.pretty(), pos=ent.field_pos['author']) for author in ent.authors()]
    authors = [biblib.algo.tex_to_ascii(author.pretty(), pos=ent.field_pos['author']) for author in ent.authors()]

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

    ret += ent['year']

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
    entry += "  number  = {{{}}},\n".format(ent['number'])
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
    entry += "  publisher = {{{}}},\n".format(ent['note'])
    entry += "  edition   = {{{}}},\n".format(ent['edition'])
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
    pass


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file', help='.bib file to process', type=str)
    arg_parser.add_argument('-o', help='options', type=str, default="bib")

    args = arg_parser.parse_args()

    try:
        bib = open(args.file, "r")

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
                    ent.key += ch
                    if ent.key not in new_id_lst:
                        break
                    ent.key = ent.key[:-1]
                new_id_lst.append(ent.key)

        for ent in ent_lst:
            ent = insert_url(ent)
            ent = change_id(ent)

            if args.o == "bib":
                s = ent2bib(ent)
            elif args.o == "latex":
                s = ent2latex(ent)
            elif args.o == "html":
                s = ent2html(ent)

            print("{}\n".format(s))

        recoverer.reraise()

    except biblib.messages.InputError:
        sys.exit(1)
