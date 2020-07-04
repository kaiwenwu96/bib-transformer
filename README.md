# bib transformer (under construction)

The purpose of the repository is to present rules and tips on bib entries and citation format when writing a paper. In addition to that, this repository also contains a simple procedure to pre-process bib entries (missing entries checking, reformatting bib entry fields, and unifying bib entries' id), which makes [this guy's](https://cs.uwaterloo.ca/~y328yu/) life easier.

I also attach some writing tips.

1. JMLR [writing instructions](http://www.jmlr.org/format/format.html)
2. Jimmy's [tips](https://github.com/lintool/guide/blob/master/writing-pet-peeves.md)

## Usage
Type `python transform.py --in_file input_file.bib --out_file output_file.bib --option bib  --loop 1` in the command line. The procedure will parse the bib file and output new bib entries to the output file.

The procedure will crash on bib files with incorrect grammar or missing required fields (e.g. author, title).

## Core Functionalities
- [x] change 'url' field into a hyper link in title
- [x] unify bib entries id (see blow) 
- [x] delete redundant fields (e.g. keywords, abstract)

## Source of Bib Entries 

Google scholar is always a default source when the official bib entry cannot be found. However, when the official bib file is available, one should avoid using google scholar. When possible, please cite a published version rather than an arXiv preprint version.

We recommend downloading bib entries from official websites. Here is a non-exhaustive list of websites.

1. For ICML, AISTATS and COLT papers, see <http://proceedings.mlr.press>
2. For NIPS papers, see <https://papers.nips.cc>
3. For ICLR papers, see <https://openreview.net>
4. For Annals of Statistics paper, see <https://projecteuclid.org/>
5. For CVPR and ICCV papers, see <http://openaccess.thecvf.com>

## General Citation Format

We list a few examples illustrate the required bib fields for different types of publications.

Cite a conference paper
```
@inproceedings{DuchiSSC2008,
  title     = {Efficient Projections onto the $\ell_1$-ball for Learning in High Dimensions},
  author    = {Duchi, John and Shalev-Shwartz, Shai and Singer, Yoram and Chandra, Tushar},
  booktitle = {Proceedings of the 25th international conference on Machine learning},
  pages     = {272--279},
  year      = {2008},
}
```

Cite a journal paper
```
@article{Dykstra1983,
  title     = {\href{https://www.jstor.org/stable/2288193}{An algorithm for restricted least squares regression}},
  author    = {Dykstra, Richard L},
  journal   = {Journal of the American Statistical Association},
  volume    = {78},
  number    = {384},
  pages     = {837--842},
  year      = {1983},
}
```

Cite a preprint
```
@preprint{Anonymous2020,
  title     = {\href{https://openreview.net/forum?id=Skgq1ANFDB}{Curvature-based Robustness Certificates against Adversarial Examples}},
  author    = {Anonymous},
  note      = {Submitted to International Conference on Learning Representations},
  year      = {2020},
}

@preprint{ManoleBW2019,
  title     = {\href{https://arxiv.org/abs/1909.07862}{Minimax Confidence Intervals for the Sliced Wasserstein Distance}},
  author    = {Manole, Tudor and Balakrishnan, Sivaraman and Wasserman, Larry},
  note      = {arXiv preprint arXiv:1909.07862}, 
  year      = {2019},
}
```

Cite a book
```
@book{BoydVandenberghe2004,
  title     = {\href{https://web.stanford.edu/~boyd/cvxbook/}{Convex optimization}},
  author    = {Boyd, Stephen and Vandenberghe, Lieven},
  publisher = {Cambridge university press},
  edition   = {1st},
  year      = {2004},
}
```

## Bib Entry Id Convention 

We have the following convention for bib entry id.
```
[author(s) last name(s)] + [year] + [possible additional suffix]
```

Here are a few examples.

Case 1: Only one author (first author's last name + year)
```
@inproceedings{Yu13,
    title={On Decomposing the Proximal Map},
    author={Yaoliang Yu},
    booktitle={Advances in Neural Information Processing Systems 27 {(NIPS)}},
    year={2013},
}
```

Case 2: Two authors (first author's last name + second author's last name + year)
```
@inproceedings{SunYu19,
  title={Least Squares Estimation of Weakly Convex Functions},
  author={S. Sun and Y. Yu},
  booktitle={International Conference on Artificial Intelligence and Statistics {(AISTATS)}},  
  year={2019},
}
```

Case 3: At least three authors (first author's last name + the initial of remaining authors' last names + year)
```
@inproceedings{WangSY19,
  title       = {Multivariate Triangular Quantile Maps for Novelty Detection},
  author      = {J. Wang and S. Sun and Y. Yu},
  booktitle   = {Advances in Neural Information Processing Systems {(NeurIPS)}},  
  year        = {2019},
  keywords    = {published},  
}
```

Case 4: If there is a conflict of id, append one additional character to distinguish them.
```
@inproceedings{Yu13a,
    title     = {Better Approximation and Faster Algorithm Using the Proximal Average},
    author    = {Yaoliang Yu},
    booktitle = {Advances in Neural Information Processing Systems 27 {(NIPS)}},
    year      = {2013},
}

@inproceedings{Yu13b,
    title     = {On Decomposing the Proximal Map},
    author    = {Yaoliang Yu},
    booktitle = {Advances in Neural Information Processing Systems 27 {(NIPS)}},
    year      = {2013},
}
```
