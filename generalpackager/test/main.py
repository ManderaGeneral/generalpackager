
import unittest

from generallibrary import get_launch_options, EnvVar


for key, value in get_launch_options().items():
    EnvVar(name=key).value = value

unittest.TextTestRunner().run(unittest.TestLoader().discover("generalpackager/test"))
