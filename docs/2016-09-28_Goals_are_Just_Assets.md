## Defining on Goals

### Concrete vs Imaginary

When you think about it, goals are no different from things, except, they are the imaginary things.

That means, in order to define a goal, we simply construct a concept, much like what we do on WikiData, when define concepts by assigning  properties.

```
>>> import asterisk as rx
>>> Universe = rx.Concept('Q1')
>>> reality = Universe({'gravitational constant': 6.67408e-11})
>>> goal = Universe({'gravitational constant': 6.69408e-11})
```

To achieve any goal, we simply search what the goal state depends on, express these dependencies as functions, plug into system of equations, and solve it for the actions to take. (Q: What does gravitational constant depend on?)

However, in order to differentiate between reality and goal, it would be convenient to have different ways to assign the property values, for example:

```
>>> reality = Universe.fact({'gravitational constant': 6.67408e-11})
>>> desirity = Universe.goal({'gravitational constant': 6.69408e-11})
```

Defining an addition operation on these concepts, would allow us to add up multiple goals to create common ``dream landscape`` (think in comparison to ``risk landscape``), and to add up multiple facts to create a picture of reality.

Ideally, this framework would allow to combine goal elements in any way we want, - either by defining many tiny goals that add up, or by defining several complex goals, that still have the addition operation defined.

Moreover, as the goals are achieved and the picture of reality changes, the concrete and imaginary then would cancel out, as described in here, in my post on [negative cardinality](http://www.halfbakery.com/idea/Negative_20Cardinality). If goals are nothing more than reality with negative cardinality, we would write:

```
>>> reality + desirity
Universe({'gravitational constant': -1.9999999999999672e-13})
```

But most poeple would find the below more straightforward:

```
>>> desirity - reality
Universe({'gravitational constant': -1.9999999999999672e-13})
```

...which in any case is the distance to the goal.

### Thinking in Tables

However, in most real life scenarios, people use table formats to arange random variables, do regressions to actually find the functional relationships, to only then set the equations to solve.

Moreover, people generally use quantitative descriptions for the ranges of variables. For example, when I was creating [StepIO](https://github.com/WeFindX/StepIO), I found out that essential characteristics about quantity, which people tend to pursue, can be characterised by:

```
  {'f_units': '',
   'f_price': '',
   'price_unit': u'usd',
   'min_units': u'10',
   'max_units': u'12',
   'min_price': u'50',
   'max_price': u'50'}
```

Where, here the ``f_units`` describe how the number of units changes within codomain ``(min_units, max_units)``, and ``f_price`` describe the behavior of price within ``(min_price, max_price)``.

In ``StepIO``, we can express everything in ``human hours`` as currency, without relying on any national currency. So, this makes it pretty general framework.

The ``StepIO`` actually describes a succession of ``Step(input, output)``, where ``input`` and ``output`` both represent sets of assets, i.e., assets to be added, and expected assets to be obtained as a result (and their respective quantities and prices to the goal pursuing entity).

## Conclusion

This brings me to conclusion, that a ``Step`` of ``StepIO`` could be defined by:

```
>>> reality = rx.Concept('Q154').fact({'units':..}) + rx.Concept('Q41').fact({'units':..) + ...
>>> goal = rx.Concept.goal('Q144')({'units':..}) + ...
>>> increment = goal-reality
>>> s1 = Step(input=increment.input, output=increment.output)
```

Constructing the ``increment`` may seem as simple as subtracting two states, and it should be. However, world is non-linear, and creativity often needs to be applied to result in deliverable (``increment.output``).  Humans solve it by imagination, in terms of efforts and their results, and computers are not very good (yet) at solving the ``increment`` decomposition into (``increment.input``, ``increment.output``) problem (to do these decompositions is often the job of C-level officals in companies). However, since the increment decomposes into movement of assets (``I/O``, in such situation it is useful to have a way to specify increments that we imagine, to let us visualize their cumulative effects, e.g.:

```
>>> input = rx.Concept('Q41')(...) + rx.Concept('Q442')(...) + ...
>>> ouput = rx.Concept('Q88')(...) + ...
>>> s1 = Step(input, output)
```

Many steps add up as cumulative sum as plan progresses, as exemplified in [PlanDF](https://github.com/wefindx/PlanDF).

```
>>> plan = Plan([s1, s2, s3,...])
```

Given that information, PlanDF computes the best/worst/most likely case scenarios, based on [BetaPert distribution](https://github.com/WeFindX/PlanDF/blob/master/docs/beta-PERT.ipynb).

However, while in **PlanDF** we had a DataFrame (plan = plandf.PlanMaker([plan_tuples]); plan.df)  with column names in one language:

```
>>> plan = plandf.PlanMaker([
    ('time: 0.75~1.2[1.]@1h', 'cake: 1~2@1h'),
    ('time: 1.5@1h', 'sandwitch: 10@0.06h'),
    ])

>>> plan.df
```

If we specify plan in terms of WikiData concepts, then they should be able to be displayed in any language:

```
>>> plan = plandf.PlanMaker([
    ('time: 0.75~1.2[1.]@1h', 'Q13276: 1~2@1h'),
    ('time: 1.5@1h', 'Q28803: 10@0.06h'),
    ])

>>> plan.df
```

Moreover, since the concepts include ``has quality`` relation (P1552) ([read here](https://github.com/mindey/asterisk/blob/master/docs/PlanDF_WikiData.ipynb)), we can use such knowledge to construct a database of imaginary and actual existing things.

Additionally, we could actually make the keys multi-indexed.
