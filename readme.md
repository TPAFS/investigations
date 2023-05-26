# Persius Investigations

This repository houses the code and data analyses for data-driven investigations and academic articles produced and maintained
by Persius. For every article we produce, our goal is to provide an accessible, transparent and open source view of the processes
and analyses we performed on raw, publicly available data in order to draw our conclusions. Our hope is that this will empower
readers and the community at large to validate and audit all of our claims and results, improve on and fix our work when there
are omissions or mistakes, and build trust in our analyses.

## Individual Investigations

Every folder in [./investigations](./investigations) corresponds (or will correspond) to an article hosted on [https://blog.persius.org/investigations](htpps://blog.persius.org/investigations).

In turn, each investigation folder will house a collection of jupyter notebooks, which will allow one to reproduce all of the data and (static) figures appearing in an article.
For those who are unable or would prefer not to actually setup a necessary environment and run the jupyter notebooks, we also provide static html outputs corresponding to the
result of running each notebook.

## Running Notebooks

For the most part, every investigation will share a base set of requirements necessary

Install python requirements in a virtual environment, e.g. via:

```bash
python3 -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt
```

from the top level of this directory.

Each notebook in each investigation should now be usable in a self-contained way.

## License

**Data, Documentation and Other Media**

The data, documentation, and media presented in this repository is licensed under <a rel="CC-BY-SA-4.0-license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

See [`LICENSE.CC-BY-SA-4.0`](./LICENSE.CC-BY-SA-4.0) for a full text copy of this license.

**Code**

All original underlying source code in this repository, including that used to validate data submissions, parse other data sources, and adapt data formats, is licensed under <a rel="apache-2.0-license" href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>.

See [`LICENSE`](./LICENSE) for a full text copy of this license.

Please start a discussion thread for any question or concerns related to licensing.

## Attribution

If you find this repository useful in your work, please consider mentioning it, providing a link, or citing it to help increase our exposure, even if you don't end up using it directly. We'd greatly appreciate that.

For those directly using this, in adhering to the attribution clause of the license governing the data, documentation and other media, you can attribute this work as "Persius Investigations Repository", and share the url: https://github.com/TPAFS/investigations

For publications that use this work, please use the following citation:

```latex
@misc{persius2022transparency,
author ={{Persius Contributors}},
title={{Investigations}},
publisher = {GitHub},
howpublished={\url{https://github.com/TPAFS/investigations}},
year={2022},
}
```
