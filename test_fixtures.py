

import os 
from utils import str_to_bool

def write_integer(string, path):
    with open(path, "w") as _f:
        try:
            _f.write(str(str_to_bool(string)))

        except RuntimeError:
            _f.write(0)



class TestWriteBooleans:


    def setup(self):
        if os.path.exists("/tmp/test_vaalue"):
            os.remove("/tmp/test_value")


    def test_write_Yes(self):
        write_integer("Yes", "/tmp/test_value")

        with open("/tmp/test_value", "r") as _f:
            value = _f.read()



        assert value == "True"



def test_write_n(self):
    write_integer("n", "/tmp/test_value")
    with open ("/tmp/test_value", "r") as _f:
        value = _f.read()


    assert value == "False"
