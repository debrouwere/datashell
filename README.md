# Data Shell

**Please note:** this is just a little experiment, don't expect too much.

If you have a statistics background, you're probably familiar with R. And if you've been using R for a while, the thing you start to appreciate most is that once you have that terminal open, you can get down to business pretty much immediately. Dumping functionality as diverse as numerical optimization, linear regression and the cumulative distribution function for a Poisson distribution all into the global namespace is _probably_ not a good idea, but boy is it useful for quick data exploration. That's what Data Shell does for Python.

Install with

```sh
pip3 install datashell
```

Open up an IPython-based data shell with by typing `datashell` into your terminal.

(If you want, you can alias it to something shorter too, by putting e.g. `alias dash=datashell` into your `~/.bashrc` or wherever your shell customizations live.)

### Convenience functions

Currently, it loads convenience functions from `numpy`, `scipy.stats`, `statsmodels`, `sympy` as well as Pandas.

All functions are lazy-loaded, so startup time is not much different than a regular IPython terminal.

Data shell does a star import of various packages into the global namespace, but also keeps them available under their respective namespaces, so you can access functionality both ways.

To give just one example, once you're in your IPython data shell, a linear regression on a dataset in your working directory is simply:

```python
ols('y ~ x', data=tables.test).fit().summary()
```

Behind the scenes, this will load `statsmodels.formulas.api.ols` to perform a linear regression, and `tables.test` will load `test.csv`.

Datashell can also be used in (non-interactive) scripts:

```python
from datashell import *
diff(2*x**2)
```

(Though at some point you'll probably want to clean things up and do proper imports.)

### Data autoloader

Data shell also includes a Pandas autoloader for CSV files: you can access a Pandas DataFrame of `./subdir/myfile.csv` from `tables.subdir.myfile`.

### Useful shortcuts

* from `random`: `shuffle`, `choice`, `sample` and friends
* from `sympy`: `expand`, `factor`, `simplify` to simplify mathematical expressions, `diff` to differentiate, `integrate` to integrate (many one-letter variables are also predefined: a-e, o-s and u-z)
* from `scipy.optimize`: `minimize`
* from `scipy.stats`: `describe`, `kurtosis`, `mode`, `moment`, `skew`, `pearsonr`, `spearmanr` and others
* from `scipy.stats.contingency`: `expected_freq`, `margins`
* from `scipy.stats.distributions`: `cdf`, `pdf`, `ppf`, `sf`, `rvs` and various other functions on statistical distributions from normal to gamma
* from `statsmodels.api`: `datasets` and `families` (for use with generalized linear models)
* from `statsmodels.formula.api`: `ols` and `gls`