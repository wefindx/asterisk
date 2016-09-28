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

def get_one(d):
    priorities = ['en', 'zh', 'de', 'ru', 'fr']
    for lang in priorities:
        if d.get(lang):
            return d[lang]
    return d.values()[0]

def Concept(wikidata_id):

    # Defining Classes Programmatically:
    # http://chimera.labs.oreilly.com/books/1230000000393/ch09.html#_defining_classes_programmatically

    _wdjson = get_json(wikidata_id)
    _alias = get_one(_wdjson['entities'][wikidata_id]['aliases'])[0]['value']

    class Name(): pass

    def _init(self, details={}):
        self.details = details

    def _repr(self):
        return '%s (%s)' % (wikidata_id, self.details)

    def _lang(self, langs=[]):
        if langs:
            s = '|'
            for lang in langs:
                val = self.__class__.wdjson['entities'][wikidata_id]['aliases'].get(lang)[0]['value']
                s += " %s |" % (val,)
            return s
        else:
            return get_one(self.__class__.wdjson['entities'][wikidata_id]['aliases'])[0]['value']

    def _unicode(self):
        return '%s (%s)' % (self.u(), self.details)

    propositions = ''

    for key in _wdjson['entities'][wikidata_id]['claims'].keys():
        for claim in _wdjson['entities'][wikidata_id]['claims'][key]:
            value = claim.get('mainsnak').get('datavalue')
            propositions += '%s : %s.%s : %s\n' % (wikidata_id, key, claim.get('type'), unicode(value))

    _doc = """%s (%s)\n\nPropositions\n============\n%s""" % (wikidata_id, _alias, propositions)

    Name.__name__ = str(wikidata_id)
    Name.wdjson = _wdjson
    for key in _wdjson['entities'][wikidata_id]['claims'].keys():
        setattr(Name, key, _wdjson['entities'][wikidata_id]['claims'][key])
    Name.__init__ = _init
    Name.__unicode__ = _unicode
    Name.__repr__ = _repr
    Name.as_languages = _lang
    Name.languages = _wdjson['entities'][wikidata_id]['aliases'].keys()
    Name.__doc__ =  _doc

    return Name
