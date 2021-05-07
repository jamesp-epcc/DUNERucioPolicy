from .path_gen import register_dune_surl_algorithm
from .lfn2pfn import register_dune_lfn2pfn_algorithm

SUPPORTED_VERSION="1.20.7"

register_dune_surl_algorithm()
register_dune_lfn2pfn_algorithm()
