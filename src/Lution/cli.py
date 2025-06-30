import argparse
from modules.configcheck.VERSION import *

parser = argparse.ArgumentParser()
parser.add_argument("about", help="about the app",)
args = parser.parse_args()
if args.about:
    print("verbosity turned on")