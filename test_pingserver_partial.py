import sys
import importlib.util
from threading import Thread
from time import sleep

new_dir = __file__.replace("\\", "/").rsplit("/", maxsplit=2)[0] + "/pingserver"
print("Full path to the pingserver folder: " + new_dir)

sys.path.append(new_dir)

spec = importlib.util.spec_from_file_location("server", new_dir + "/server.py")
server_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server_module)

spec = importlib.util.spec_from_file_location("db_manager", new_dir + "/db_manager.py")
db_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(db_module)

def test_increase_address():
    start = "23.42.0.0"
    increased = "23.43.0.0"
    assert increased == server_module.Server._increase_address(start)

def test_write_to_db():
    Thread(target=server_module.INSTANCE._write_to_db, daemon=True).start()

    server_module.INSTANCE.add_to_db.append("23.224.25.34")
    server_module.INSTANCE.add_to_db.append("32.242.135.44")
    server_module.INSTANCE.add_to_db.append("223.64.74.24")

    sleep(10)

    assert db_module.get_addresses() == ["23.224.25.34", "32.242.135.44", "223.64.74.24"]
