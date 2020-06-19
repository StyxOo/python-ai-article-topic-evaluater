from . import sgm_reader
from . import rewrite


def process():
    sgm_reader.main()
    rewrite.main()
