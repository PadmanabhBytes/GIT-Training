import os
import sys
from datetime import datetime


def check_date():
    print(datetime.now())
    print(os.getcwd())
    return sys.platform
