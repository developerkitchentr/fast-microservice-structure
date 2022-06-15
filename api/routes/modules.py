
from leanapi.server import Modules
from .foo.foo import Foo

modules = Modules.controllers([Foo])
