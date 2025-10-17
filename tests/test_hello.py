import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.hello import say_hello

def test_say_hello():
    assert say_hello() == "Hello, Worฟld!"


