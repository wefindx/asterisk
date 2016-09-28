# -*- coding: utf-8 -*-
import json
import requests

BASE_URL = 'https://www.wikidata.org/w/api.php'

def get_json(wikidata_id):
    url = 'https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&format=json' % (wikidata_id,)
    dicts = json.loads(requests.get(url).content)
    try:
        dicts = json.loads(requests.get(url).content)
        return dict(dicts, **{'success': True})
    except:
        {'success': False}

def get_lang(d):
    priorities = ['en', 'zh', 'de', 'ru', 'fr']
    for lang in priorities:
        if d.get(lang):
            return d[lang]
    return d.values()[0]

def Concept(wikidata_id):

    # Defining Classes Programmatically:
    # http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_defining_classes_programmatically

    _concept = get_json(wikidata_id)
    _alias = get_lang(_concept['entities'][wikidata_id]['aliases'])[0]['value']

    class Name(): pass

    def _init(self, details={}):
        self.details = details

    def _repr(self):
        if self.details:
            return '%s (%s)' % (wikidata_id, self.details)
        else:
            return str(wikidata_id)

    def _lang(self, *args):
        if len(args) > 1:
            s = {}
            for lang in args:
                val = self.__class__.concept['entities'][wikidata_id]['aliases'].get(lang)[0]['value']
                s[lang] = val
            return s
        elif len(args) == 1:
            return self.__class__.concept['entities'][wikidata_id]['aliases'].get(args[0])[0]['value']
        else:
            return get_lang(self.__class__.concept['entities'][wikidata_id]['aliases'])[0]['value']

    def _unicode(self):
        return '%s (%s)' % (self.u(), self.details)

    propositions = ''

    for key in _concept['entities'][wikidata_id]['claims'].keys():
        for claim in _concept['entities'][wikidata_id]['claims'][key]:
            value = claim.get('mainsnak').get('datavalue')
            propositions += '%s : %s.%s : %s\n' % (wikidata_id, key, claim.get('type'), unicode(value))

    _doc = """%s (%s)\n\nPropositions\n============\n%s""" % (wikidata_id, _alias, propositions)

    Name.__name__ = str(wikidata_id)
    Name.concept = _concept
    for key in _concept['entities'][wikidata_id]['claims'].keys():
        setattr(Name, key, _concept['entities'][wikidata_id]['claims'][key])
    Name.__init__ = _init
    Name.__unicode__ = _unicode
    Name.__repr__ = _repr
    Name.lang = _lang
    Name.languages = _concept['entities'][wikidata_id]['aliases'].keys()
    Name.__doc__ =  _doc

    return Name

def Instance(wikidata_id):
    return Concept(wikidata_id)()
