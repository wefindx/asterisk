# Initially, I think:

```
import asterisk as ri

ri.Concept  # wikidata concepts
ri.Y        # for defining goal sate
ri.X        # for defining possible actions
ri.F        # for defining world state
ri.Process  # for defining agent (ai.py)
ri.oo       # Infinity categories
ri.oo.Goal  # Infinity goal.
ri.oo.Idea  # Infinity idea.
ri.oo.Plan  # for defining sequence of Steps
ri.oo.Step  # for defining steps of IO

# *Infinity will help to align personal goals with world's goals, as ri.Y would be conditioned on ri.oo.Goal.
```

As this would enable us to construct plans from Concepts. The concept could be instantiated by providing a WikiData ID, and this way, automatically become an ``class`` representable in many languages, and with many properties. From a concept, instances could be derived.

## So that we can define new things like so:

```
# By default, we are using WikiData IDs, see docstring for documentation, if using something else.

>>> Dog = ri.Concept('Q1')
>>> d = Dog(color='brown')
>>> d.color
brown

# World already has concepts, so we don't have to re-invent them.
```

## And define new hypothetical steps like so:

```
>>> s1 = ri.oo.Step({'in': '...any assets of input...', 'out': '...any assets of output...'})
>>> s2 = ri.oo.Step({'in': '...any assets of input...', 'out': '...any assets of output...'})
```

## And definition of plan like so:

```
>>> p = ri.oo.Plan(steps=[s1, s2])
```

This would then give us estimate of value over time, and we could add this as a suggestion for agent:

## Instantiating optimizing agent:

```
agent = ri.Process(world=ri.F(), actions=ri.X(), goal=ri.Y())
```
