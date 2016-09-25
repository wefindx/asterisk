import json
import requests

BASE_URL = 'https://www.wikidata.org/w/api.php'

def get_wikidata_json(concept_id):
    url = 'https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&format=json' % (concept_id,)
    dicts = json.loads(requests.get(url).content)
    try:
        dicts = json.loads(requests.get(url).content)
        return dict(dicts, **{'success': True})
    except:
        {'success': False}

def get_concept(concept_id=''):
    class Name():
        def __init__(self):
            pass
    return Name
