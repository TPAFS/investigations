# Persius Investigations

This repository houses the code and analyses for investigations and articles produced and maintained
by [Persius](https://github.com/TPAFS).

For every article we produce, our goal is to provide an accessible, transparent and open source view of the processes
and analyses we performed on raw, publicly available data in order to draw our conclusions.

Our hope is that this will empower readers and the community at large to:

- Validate and audit all of our claims and results.
- Improve on and fix our work in case of omissions or mistakes.
- Build trust in our analyses.

## Individual Investigations

Every folder in [./investigations](./investigations) corresponds to an article hosted on [https://blog.persius.org/investigations](htpps://blog.persius.org/investigations).

Each folder will house a collection of code and artifacts such as preprocessing logic, jupyter notebooks, plots, etc., which will allow one to reproduce all of the data, analyses and (static) figures appearing in an article.

For those who are unable or would prefer not to actually setup a necessary environment to run the jupyter notebooks, the notebook outputs are retained, and can be
viewed without setup.

## Running Notebooks

Every investigation will share a base set of necessary python requirements, which are recorded in the
top level `requirements.txt`. Individual investigations may additionally specify their own _additional_
requirements; when necessary, a `requirements.txt` file will be present in the top level of the
investigation subdirectory.

Install python requirements in a virtual environment, e.g. via:

```bash
python3 -m venv .env
source ./.env/bin/activate
pip install -r requirements.txt
```

from the top level of this directory.

Each notebook in each investigation should now be usable in a self-contained way.

## Contributing

We welcome contributions from all, and constructive feedback and discussion of any form.

Please see [./.github/CONTRIBUTING.md](./.github/CONTRIBUTING.md) for more information about how to contribute to this project, or head to the github Discussions tab to join or start a conversation.
## License

**Data, Documentation and Other Media**

All _original_ data, documentation, and media presented in this repository is licensed under <a rel="CC-BY-SA-4.0-license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>. For data that we parse and analyze that is unoriginal, please consult the primary sources for licensing information.

See [`LICENSE.CC-BY-SA-4.0`](./LICENSE.CC-BY-SA-4.0) for a full text copy of this license.

**Code**

All original underlying source code in this repository, including that used to plot, validate, parse
or adapt data, is licensed under <a rel="apache-2.0-license" href="https://www.apache.org/licenses/LICENSE-2.0">Apache 2.0 License</a>.

See [`LICENSE`](./LICENSE) for a full text copy of this license.

Please start a discussion thread for any question or concerns related to licensing.

## Attribution

If you find this repository useful in your work, please consider mentioning it, providing a link, or citing it to help increase our exposure, even if you don't end up using it directly. We'd greatly appreciate that.

For those directly using this, in adhering to the attribution clause of the license governing the data, documentation and other media, you can attribute this work as "Persius Investigations Repository", and share the url: https://github.com/TPAFS/investigations

For publications that use this work, please use the following citation:

```latex
@misc{persius2023investigations,
author ={{Persius Contributors}},
title={{Investigations}},
publisher = {GitHub},
howpublished={\url{https://github.com/TPAFS/investigations}},
year={2023},
}
```
