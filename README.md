[![Travis status](https://img.shields.io/travis/mindey/asterisk/master.svg?style=flat)](https://travis-ci.org/mindey/asterisk)
# Asterisk
Tools for computing asset risk with respect to goals.

Today advanced decision-making and artificial intelligence techniques are used primarily by financial and security industries. This is an attempt to create a tool that would be useful to apply the advanced decision-making techniques for people's personal lives, with respect to any goals, and any assets. We learned math at school, so let's apply it not only at work, but also at home.

    pip install asterisk                                          (only Python2.7 for now)

Asterisk implements a wrapper on top of the WikiData API, as a source for schemas of objects, so that we could automatically have multilingual, well-defined concepts, with respect to which to define assets. Then, it will use the functionality of packages ``stepio`` and ``plandf``, and more, to provide the means to create computable, multilingual, hierarchial plans.

## Examples

Plans defined with "Q" retrieve and map schemas from WikiData. E.g., [Q144](https://www.wikidata.org/wiki/Q144) is a dog, and [Q146](https://www.wikidata.org/wiki/Q144) is a cat. When instantiating an item from schema, by default, the ``.fact=False``, and the instances are prepended with asterisk ``*``, meaning that it is something hypothesized, not really existing. If the thing that you are instantiating actually exists in real life (e.g., a specific human, a specific loan), pass the ``.fact=True`` (and you can also add attribute such as ``Lithuania's republic passport ID``, or ``Bondora loan ID`` to provide actual reference to identify with real thing.) The real things are prepended with dot ``.`` rather than asterisk.

You can define a goal as a set of assets within an output of a step, part of plan. At the moment. the .Plan does not yet work, but you can already instantiate lists like:

```{python}
import asterisk as rx

# Concepts
Dog = rx.Concept('Q144')
Cat = rx.Concept('Q146')
Human = rx.Concept({'en': 'human', 'lt': u'žmogus', 'zh': u'人'})
Family = rx.Concept({'en': 'family', 'de': 'Familie', 'lt': 'šeima'})
Dollar = rx.Concept({'en': 'US Dollar'})

# Instances (Assets)
alice = Human({'name': 'Alice', 'legs': 2, 'person_id': 'LT123148188101041041'}, fact=True)
bob = Human({'name': 'Bob', 'legs': 2, 'person_id': 'EE18416109410238120'}, fact=True)
dog = Dog({'name': 'Tako', 'legs': 4, 'owner': bob})
cat = Cat({'legs': 4, 'owner': alice})
family = Family({'name': "Alice and Bob's family", 'mission': "To enjoy each other's minds, activities together, and exploration of the Universe."})
dollar = Dollar()

# List of Steps
[
    {'input': {alice: 1, bob: 1},
    'output': {family: 1}
    },
    
    {'input': {dollar: 200},
    'output': {cat: 1}},

    {'input': {dollar: 250},
    'output': {cat: 1}}
]
```

### Future:

```{python}
# Future: Multilingual plans with respect to defined concepts, display-able and computable...
plan = rx.Plan(
    [
        {'input': {alice: 1, bob: 1},
        'output': {family: 1}
        },
        {'input': [
            {'input': {dollar: 200},
            'output': {cat: 1}},

            {'input': {dollar: 250},
            'output': {cat: 1}}
            ],
         'output': 'compute'
         }
    ]
)

plan.risk()
```
