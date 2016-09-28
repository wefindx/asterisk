# Initial Thoughts.

During the development of [Infinity](https://github.com/WeFindX/infinity), it occurred to me, that several things related to estimation of plan risk and concept instances with respect to which we compute risk, could be useful as a separate package.

I came to this realization after studying a little more the scientific stack of Python. Namely, I realized that the core subset of things available in [Maple language]() and core of [R language](), are implemented in Python very nicely by ``matplotlib``, ``pandas``, ``scipy.stats`` and ``statsmodels``, and can be imported as:

```
%matplotlib inline
import sympy as S
import pandas as pd
import scipy.stats as st
import statsmodels.api as sm
```

I think of implementing this package in context of these packages, which encapuslate also ``numpy``. Moreover, I am thinking that probably I should also use the ``xarray`` by Pydata instead of ``Pandas``, because it supports multi-dimensional labeled data, but I want to start with ``Pandas``, which I know well.

I would ``import asterisk as rx``. It associates well with "risk", and is easy to type.

## What I Want to Include First.

### A Couple of Things That I Already Have.
- Include as of yet unpublished most general artificial intelligence agent automation framework ([ai.py](#)).
- Concept retrieval and usage to display in many languages from [WikiData](https://wikidata.org).
- Currency value retrieval from opencurrencyrates and other places.
- Value of human time retrieval from info about average wages from [FRED](https://fred.stlouisfed.org/) (to be optional).
- Value over time computation from [StepIO](https://github.com/WeFindX/StepIO) and [PlanDF](https://github.com/WeFindX/PlanDF).

### A Couple of Things That I Don't Yet Have.
- Extend the value over time computation DataFrame ``PlanDF`` by use of Pandas ``MultiIndexes``.
- Interface for retrieving market values of any assets (an abstract class for making data retrieval routines).
- Interface with any database, that stores records about any assets (asset bank).
- Rewrite these things with tests.

## Final Product.

The final product is quite simple - it would be a tool that allows anyone to define a goal in terms of concepts, make plans, estimate their risk, ROIs in terms of reduction of distance to their goal, and publish plan on [infinity](https://infty.xyz)? :)
