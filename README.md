[![Travis status](https://img.shields.io/travis/mindey/asterisk/master.svg?style=flat)](https://travis-ci.org/mindey/asterisk)
# Asterisk
Tools for computing asset risk with respect to goals.

Today advanced decision-making and artificial intelligence techniques are used primarily by financial and security industries. This is an attempt to create a tool that would be useful to apply the advanced decision-making techniques for people's personal lives, with respect to any goals, and any assets. We learned math at school, so let's apply it not only at work, but also at home.

    pip install asterisk

(Currently only on Python 2.7, will extend and add tests soon.)

It will depend on ``pandas``, ``sympy``, and a few more packages.

## Examples

```{python}
import asterisk as rx

# Concepts
Dog = rx.Concept('Q144')
Cat = rx.Concept('Q146')
Human = rx.Concept({'en': 'human', 'lt': u'žmogus', 'zh': u'人'})
Family = rx.Concept({'en': 'family', 'de': 'Familie', 'lt': 'šeima'})
Dollar = rx.Concept({'en': 'US Dollar'})

# Instances (Assets)
alice = Human({'name': 'Alice', 'legs': 2})
bob = Human({'name': 'Bob', 'legs': 2})
dog = Dog({'name': 'Tako', 'legs': 4, 'owner': bob})
cat = Cat({'legs': 4, 'owner': alice})
family = Family({'name': "Alice and Bob's family", 'mission': "To enjoy each other's minds, activities together, and exploration of the Universe."})
dollar = Dollar()

# Future: Multilingual plans with respect to defined concepts, display-able and computable...
plan = rx.Plan(
    [
        {'input': {alice: 1, bob: 1},
        'output': {family: 1}
        },

        {'input': {dollar: 200},
        'output': {cat: 1}},

        {'input': {dollar: 250},
        'output': {cat: 1}}
    ]
)

plan.risk()
```
