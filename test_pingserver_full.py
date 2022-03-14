import os
import socket
from threading import Thread
from time import sleep
from socket import create_connection

def test_get_request():
    local_address = socket.gethostbyname(socket.gethostname())
    main_file = __file__.replace("\\", "/").rsplit("/", maxsplit=2)[0] + "/pingserver/main.py"
    Thread(target=os.system, args=("python3 " + main_file + " -a " + local_address,), daemon=True).start()
    sleep(3)

    assert _get_address(local_address) == "1.1.0.0"
    assert _get_address(local_address) == "1.2.0.0"
    assert _get_address(local_address) == "1.3.0.0"
    assert _get_address(local_address) == "1.4.0.0"
    assert _get_address(local_address) == "1.5.0.0"

def _get_address(local_address):
    sock = create_connection((local_address, 20005))
    _send(sock, "GET address")
    return _recv(sock)

def _send(sock, text):
    """Send string to the given socket"""

    sock.send(_string_to_bytes(text))

def _recv(sock):
    """Receive string from the given socket"""

    return _bytes_to_string(sock.recv(4096))

def _string_to_bytes(input_text):
    """Convert string to bytes object"""

    return bytes(input_text, 'utf-8')

def _bytes_to_string(input_bytes):
    """Convert bytes object to string"""

    return input_bytes.decode()
