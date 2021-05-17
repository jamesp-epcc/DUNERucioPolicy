#from .path_gen import register_dune_surl_algorithm
from .lfn2pfn import lfn2pfn_DUNE

SUPPORTED_VERSION="1.20.7"

def get_lfn2pfn_algorithms():
    return { 'DUNE': lfn2pfn_DUNE }

#register_dune_surl_algorithm()
#register_dune_lfn2pfn_algorithm()
