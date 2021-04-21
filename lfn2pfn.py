#!/usr/bin/env python

try:
    # py3
    import urllib.request as urllib2
except ImportError:
    # py2
    import urllib2
import json
from datetime import datetime

from rucio.common import config
from rucio.rse.protocols.protocol import RSEDeterministicTranslation

metacat_base = None

def lfn2pfn_DUNE(scope, name, rse, rse_attrs, protocol_attrs):
    def get_metadata_field(metadata, field):
        if field in metadata:
            return metadata[field]
        return 'None'

    # FIXME: check to see if PFN is already stored in Rucio's metadata DB
    # if so, just return it from there

    f = urllib2.urlopen(metacat_base + "app/data/file?name=" + urllib2.quote(name, ''))
    jsondata = json.load(f)
    f.close()

    metadata = jsondata['metadata']

    lfnbits = lfn.split(':')

    # determine year from timestamps
    timestamp = None
    if 'core.start_time' in metadata:
        timestamp = metadata['core.start_time']
    elif 'core.end_time' in metadata:
        timestamp = metadata['core.end_time']
    elif 'created_timestamp' in jsondata:
        timestamp = jsondata['created_timestamp']
        if timestamp is None:
            year = 'None'
    else:
        dt = datetime.utcfromtimestamp(timestamp)
        year = str(dt.year)

    # determine hashes from run number
    run_number = 0
    if 'core.runs' in metadata:
        run_number = int(metadata['core.runs'][0])
        
    hash1 = "%02d" % ((run_number // 1000000) % 100)
    hash2 = "%02d" % ((run_number // 10000) % 100)
    hash3 = "%02d" % ((run_number // 100) % 100)
    hash4 = "%02d" % (run_number % 100)

    run_type = get_metadata_field(metadata, 'core.run_type')
    data_tier = get_metadata_field(metadata, 'core.data_tier')
    file_type = get_metadata_field(metadata, 'core.file_type')
    data_stream = get_metadata_field(metadata, 'core.data_stream')
    data_campaign = get_metadata_field(metadata, 'DUNE.campaign')
    filename = lfnbits[-1]
    
    pfn = 'pnfs/dune/tape_backed/dunepro/' + run_type + '/' + data_tier + '/' + year + '/' + file_type + '/' + data_stream + '/' + data_campaign + '/' + hash1 + '/' + hash2 + '/' + hash3 + '/' + hash4 + '/' + filename

    # FIXME: store the PFN in Rucio metadata for next time
    return pfn


def register_dune_lfn2pfn_algorithm():
    global metacat_base
    RSEDeterministicTranslation.register(lfn2pfn_DUNE, 'DUNE')
    metacat_base = config.config_get('policy', 'metacat_base_url')
    if not metacat_base:
        metacat_base = 'https://dbdata0vm.fnal.gov:9443/dune_meta_demo/'
