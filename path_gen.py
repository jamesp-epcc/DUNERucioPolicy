import requests
import urllib
from rucio.common import config
from rucio.common.utils import register_surl_algorithm
from rucio.common.exception import ServiceUnavailable

sam_base = None

def construct_surl_dune(dsn, name):
    url = '%s/files/name/%s/destination?format=json' % (sam_base, urllib.quote(name, ''))

    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()
    except Exception as ex:
        raise ServiceUnavailable("Error querying SAM")

    destination = result["destination"]
    if not destination.startswith('/'):
        destination = '/' + destination
    if destination.endswith('/'):
        destination += name
    else:
        destination += '/' + name
    return destination

def register_dune_surl_algorithm():
    global sam_base
    register_surl_algorithm(construct_surl_dune, 'dune')
    sam_base = config.config_get('policy', 'sam_base_url')
    if not sam_base:
        sam_base = 'https://samweb.fnal.gov:8483/sam/dune-test/api'
