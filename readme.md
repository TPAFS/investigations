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
