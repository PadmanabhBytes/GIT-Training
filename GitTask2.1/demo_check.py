import os
import sys


def bad_formatting():
    x = {"a": 1, "b": 2}
    print(
        "This line is very long and has bad formatting and uses double quotes instead of single quotes which black prefers usually depending on settings but mostly it handles wrapping"
    )
