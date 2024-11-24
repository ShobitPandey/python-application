# test_app.py
import pytest

def hello_world():
    print("Hello, world!")

# Test function using capsys fixture to capture output
def test_hello_world(capsys):
    hello_world()
    
    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the printed output is as expected
    assert captured.out.strip() == "Hello, world!"
