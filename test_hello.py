import pytest
from hello import hello_world
from io import StringIO
from unittest.mock import patch

def test_hello_world_output():
    with patch('sys.stdout', new=StringIO()) as fake_out:
        hello_world()
        assert fake_out.getvalue().strip() == "Hello World!"
        
