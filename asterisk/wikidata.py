# -*- coding: utf-8 -*-
import json
import requests

BASE_URL = 'https://www.wikidata.org/w/api.php'

def get_json(wikidata_id):
    try:
        dicts = json.loads(
            requests.get(BASE_URL,
                params={'action': 'wbgetentities',
                        'ids': wikidata_id,
                        'format': 'json'}
            ).content)
        return dict(dicts, **{'success': True})
    except:
        return {'success': False}

def get_lang(d, languages=['en', 'zh', 'de', 'ru', 'fr']):
    ''' 
    INPUT
    d :         dictionary with keys as language codes
    languages:  list of language codes in a priority descending order

    OUTPUT
    value of the first key that's available, or the first existing key, 
    if none of the preferred languages are available

    EXAMPLE
    >>> get_lang({'en': 'love', 'zh': u'爱'}) 
    love 
    '''
    for lang in languages:
        if d.get(lang):
            return d[lang]
    return d.values()[0]

def Concept(wikidata_id):

    '''
    INPUT
    The wikidata ID (str), or (dict). If there is no internet connection 
    to WikiData API, you can simply pass a dict.

    OUTPUT
    class of WikiData type

    EXAMPLES

    >>> Dog1 = Concept('Q144')
    >>> Dog1
    <class asterisk.wikidata.Q144 at 0x7fc2b498c188>
    >>> Dog2 = Concept({'en': 'dog', 'lt': u'šuo'})
    >>> Dog2
    <class asterisk.wikidata.Q0 at 0x7fc2b43853f8>

    In the second case, the class is always of 'Q0' type, which does not 
    correspond to any WikiData concept. However, objects derived from both 
    types then have representations based on their languages. For example:

    >>> d1 = Dog1()
    >>> d1
    狗
    >>> d2 = Dog2()
    >>> d2
    šuo

    The derived objects can have different representations, and default 
    languages are specified in .languages attribute, e.g.:

    >>> d2.languages
    ['lt', 'en']

    The value is returned in the order of .languages: 

    >>> d2.set_langs(['en', 'lt'])
    >>> d2

    The first available language specified is returned, or if it is not 
    available, the first available language is returned:

    >>> d1.set_langs([])
    >>> d1
    σκυλί

    The WikiData information about claims and aliases is available in 
    .claims and .aliases respectively:

    >>> d1.aliases
    {u'el': [{u'value': u'\u03c3\u03ba\u03c5\u03bb\u03af', u'language': u'el'}...
    >>> d1.claims
    {u'P646': [{u'type': u'statement', u'references': [{u'snaks': {...
    >>> d2.aliases
    {'lt': [{'value': u'\u0161uo'}], 'en': [{'value': 'dog'}]}
    >>> d2.claims
    {}

    Additionally, each claim (property) is available as an attribute, 
    for example 'Q189539' represents a loan,

    >>> Loan = Concept('Q189539')

    We can know that loans have qualitiy (P1552) of:

    >>> Loan.P1552
    interest rate
    lender
    issue date
    Term
    Collateral
    Debtor
    entity
    quantity

    The knowledge of qualities may allow us to formulate goals, and know 
    in advance, what to look for in this type of things.

    Each property, in turn, can have nested information provided about 
    itself in terms of P and Q values.

    We can create instances with details

    >>> l1 = Loan({'lender': 'John', 'debtor': 'Julia', 'amount': 1000})
    >>> l1
    préstamo ({'lender': 'John', 'debtor': 'Julia', 'amount': 1000})
    
    Now, we will later implement the method "save" to save the instances 
    to general database as:

    >>> l1.save()

    This will allow to keep one database of any things. As described in the 
    ``ai.py``, we could use several custom constructors to record the Goals 
    and Facts about the world:

    >>> imaginary_loan = Loan.goal({'lender': 'John', 'debtor': 'Julia', 'amount': 1000})
    >>> actual_loan = Loan.fact({'lender': 'John', 'debtor': 'Julia', 'amount': 1000})

    Or:

    >>> Spaceship = Concept('Q40218')
    >>> imaginary_spaceship = Spaceship.goal({'tons to Low-Earth Orbit': 500})
    >>> existing_spaceship = Spaceship.fact({'tons to Low-Earth Orbit': 10})

    '''

    # Defining Classes Programmatically:
    # http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_defining_classes_programmatically

    if isinstance(wikidata_id, str):
        _concept = get_json(wikidata_id)
    elif isinstance(wikidata_id, dict):
        _concept = {'entities': {'Q0': {'aliases': {v:[{'value':wikidata_id[v], 'language': v}] for k,v in enumerate(wikidata_id)}, 'claims': {} }} }
        wikidata_id = 'Q0'
    else:
        return None 

    _languages = _concept['entities'][wikidata_id]['aliases'].keys()
    _popular = ['en', 'es', 'de', 'fr', 'ru', 'zh']
    _alias = get_lang(_concept['entities'][wikidata_id]['aliases'], _popular)[0]['value']

    _aliases = '|'
    for k,v in enumerate(_concept['entities'][wikidata_id]['aliases']):
        l = _concept['entities'][wikidata_id]['aliases'][v][0]
        _aliases += ' %s: %s |' % (l['language'], l['value'])

    class Name(): pass

    def _init(self, details={}, fact=False):
        self.details = details
        self.fact = fact
        if self.fact:
            self.sign = '.'
        else:
            self.sign = '*'
        self.alias = _alias
        self.aliases = self.__class__.concept['entities'][wikidata_id]['aliases']
        self.claims = self.__class__.concept['entities'][wikidata_id]['claims']

    def _neg(self):
        return self

    def _set_langs(self, language_codes):
        '''
        INPUT
        languages a list of language codes, in order of priority to be displayed 
        if exists

        OUTPUT
        sets the .alias, which is used in __repr__
        '''
        self.languages = language_codes
        self.alias = get_lang(self.aliases, self.languages)[0]['value']

    def _repr(self):
        if self.details:
            return ('%s%s (%s)' % (self.sign, self.alias, self.details)).encode('utf8')
        else:
            return ('%s%s' % (self.sign, self.alias)).encode('utf8')

    def _unicode(self):
        return '%s%s' % (self.sign, self.alias,)

    propositions = ''

    for key in _concept['entities'][wikidata_id]['claims'].keys():
        setattr(Name, key, _concept['entities'][wikidata_id]['claims'][key])
        for claim in _concept['entities'][wikidata_id]['claims'][key]:
            value = claim.get('mainsnak').get('datavalue')
            propositions += '%s : %s\n' % (key, unicode(value))

    qualities = ''
    HAS_QUALITY = 'P1552'

    if HAS_QUALITY in _concept['entities'][wikidata_id]['claims'].keys():
        for claim in _concept['entities'][wikidata_id]['claims'][HAS_QUALITY]:
            key = claim.get('mainsnak').get('datavalue').get('value').get('id')
            setattr(Name, key, claim.get('mainsnak'))
            qualities += '%s : %s\n' % (key, unicode(claim))

    _doc = """%s (%s)\n\nPropositions\n============\n%s\n\nQualities (P1552)\n=================\n%s""" % (wikidata_id, _aliases, propositions, qualities)

    Name.__name__ = str(wikidata_id)
    Name.concept = _concept
    Name.__init__ = _init
    Name.__unicode__ = _unicode
    Name.__repr__ = _repr
    Name.set_langs = _set_langs
    Name.languages = _languages
    Name.__doc__ =  _doc
    Name.__neg__ = _neg

    return Name

def Instance(wikidata_id):
    concept = Concept(wikidata_id)
    if concept:
        return concept()
    else:
        return None
