#! python3.11

from .__404__ import Page404
from .__dev__ import PageDev
from .root import PageRoot

default_pages = [Page404, PageDev, PageRoot]
default_paths = [str(i()) for i in default_pages]
