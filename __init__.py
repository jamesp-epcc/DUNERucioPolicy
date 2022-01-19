from .path_gen import construct_surl_dune
from .lfn2pfn import lfn2pfn_DUNE

SUPPORTED_VERSION="1.20.7"

def get_algorithms():
    return { 'lfn2pfn': { 'DUNE': lfn2pfn_DUNE }, 'surl': { 'DUNE': construct_surl_dune } }
