import argparse
from commands import about, sigma

parser = argparse.ArgumentParser(prog="lution")
subparsers = parser.add_subparsers(dest="command")

about = subparsers.add_parser("about", help="Info about the app")
about.set_defaults(func=about.run)

sigmacm = subparsers.add_parser("SIGMA", help="Run sigma command")
sigmacm.set_defaults(func=sigma.run)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
