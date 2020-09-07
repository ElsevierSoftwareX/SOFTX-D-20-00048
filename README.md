[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/pcafold/badge/?version=latest)](https://pcafold.readthedocs.io/en/latest/?badge=latest)

# PCAfold

**PCAfold** is a Python software for generating, improving and analyzing empirical
low-dimensional manifolds obtained via *Principal Component Analysis* (PCA).
It incorporates a variety of data pre-processing tools (including data clustering
and sampling), uses PCA as a dimensionality reduction technique and introduces
metrics to judge the topology of the low-dimensional manifolds.

## [PCAfold documentation](https://pcafold.readthedocs.io/en/latest/) at Read the Docs

Software documentation contains a thorough user guide including equations, references and example code snippets. Numerous illustrative tutorials and demos are presented as well. The corresponding Jupyter notebooks can also be found in the `docs/tutorials` directory.

## Software architecture

A general overview for using **PCAfold** modules is presented in the diagram
below:

![Screenshot](docs/images/PCAfold-software-architecture.png)

Each module's functionalities can also be used as a standalone tool for
performing a specific task and can easily combine with techniques outside of
this software, such as K-Means algorithm or Artificial Neural Networks.

## Installation

### Dependencies

**PCAfold** requires `python3.7` and the following packages:

- `copy`
- `Cython`
- `matplotlib`
- `numpy`
- `random`
- `scipy`

### Build from source

Clone the `PCAfold` repository and move into the `PCAfold` directory created:

```
git clone http://gitlab.multiscale.utah.edu/common/PCAfold.git
cd PCAfold
```

Run the `setup.py` script as below to complete the installation:

```
python3.7 setup.py install
```

You are ready to `import PCAfold`!

### Testing

To run regression tests from the base repo directory run:

```
python3.7 -m unittest discover
```

To switch verbose on, use the `-v` flag.

All tests should be passing. If any of the tests is failing and you can’t sort
out why, please open an issue on [GitLab](https://gitlab.multiscale.utah.edu/common/PCAfold).

## Authors and contacts

- **Kamila Zdybał**, *Université Libre de Bruxelles*, `Kamila.Zdybal@ulb.ac.be`
- **Elizabeth Armstrong**, *The University of Utah*, `Elizabeth.Armstrong@chemeng.utah.edu`
- **Alessandro Parente**, *Université Libre de Bruxelles*, `Alessandro.Parente@ulb.ac.be`
- **James C. Sutherland**, *The University of Utah*, `James.Sutherland@chemeng.utah.edu`
