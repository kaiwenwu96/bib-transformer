# bib transformer (under construction)

## Usage
Type `python transform.py test.bib` in the command line. The procedure will parse the bib file and output new bib entries in the command line. Redirect the output to a file if you want to (e.g. python transform.py test.bib > new-test.bib).

The procedure will crash on bib files with incorrect grammar or missing required fields (e.g. author, title).

## Functionalities
- [x] change 'url' field into a hyper link in title
- [x] change id of bib entry 
- [x] delete redundant fields (e.g. keywords)

## General Citation Format

Cite a conference paper
```
@inproceedings{TramerBoneh2019,
  title     = {\href{http://papers.nips.cc/paper/8821-adversarial-training-and-robustness-for-multiple-perturbations.html}{Adversarial Training and Robustness for Multiple Perturbations}},
  author    = {Tramer, Florian and Boneh, Dan},
  booktitle = {Advances in Neural Information Processing Systems 32},
  pages     = {5858--5868},
  year      = {2019},
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

All fields above are mandatory.

## Naming Convention

We have the following convention for bib entry id.
```
[author(s) last name(s)] + [year]
```

Here are a few examples.

Only one author (first author's last name + year)
```
@inproceedings{Yu13,
    title={On Decomposing the Proximal Map},
    author={Yaoliang Yu},
    booktitle={Advances in Neural Information Processing Systems 27 {(NIPS)}},
    year={2013},
}
```

Two authors (first author's last name + second author's last name + year)
```
@inproceedings{SunYu19,
  title={Least Squares Estimation of Weakly Convex Functions},
  author={S. Sun and Y. Yu},
  booktitle={International Conference on Artificial Intelligence and Statistics {(AISTATS)}},  
  year={2019},
}
```

At least three authors (first author's last name + the initial of remaining authors' last names + year)
```
@inproceedings{WangSY19,
  title       = {Multivariate Triangular Quantile Maps for Novelty Detection},
  author      = {J. Wang and S. Sun and Y. Yu},
  booktitle   = {Advances in Neural Information Processing Systems {(NeurIPS)}},  
  year        = {2019},
  keywords    = {published},  
}
```

If there is a conflict of id, append one additional character to distinguish them.
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

## Additional Remarks

We recommand that download bib entries from official websites (e.g. proceedings.mlr.press and nips.cc, openreview.net) rather than google scholar.
