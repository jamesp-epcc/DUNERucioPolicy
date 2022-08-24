from .path_gen import construct_surl_dune_sam, construct_surl_dune_metacat
from .lfn2pfn import lfn2pfn_DUNE

SUPPORTED_VERSION="1.26.9"

def get_lfn2pfn_algorithms():
    return { 'DUNE': lfn2pfn_DUNE }

def get_surl_algorithms():
    return { 'DUNE_sam': construct_surl_dune_sam,
             'DUNE_metacat': construct_surl_dune_metacat }
