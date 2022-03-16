"""Module containing tests testing parts of the pingserver"""

import sys
import importlib.util

# pylint: disable=W0212

new_dir = __file__.replace("\\", "/").rsplit("/", maxsplit=2)[0] + "/pingserver"
print("Full path to the pingserver folder: " + new_dir)

sys.path.append(new_dir)

spec = importlib.util.spec_from_file_location("server", new_dir + "/server.py")
server_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server_module)

def test_increase_address():
    """Test the _increase_address method"""

    start = "23.42.0.0"
    increased = "23.43.0.0"
    assert increased == server_module.Server._increase_address(start)
