import argparse
from commands import about, sigma, fflags

parser = argparse.ArgumentParser(prog="lution")
subparsers = parser.add_subparsers(dest="command")

# the about command
aboutc = subparsers.add_parser("about", help="Info about the app")
aboutc.set_defaults(func=about.run)

# the sigma command
sigmacm = subparsers.add_parser("SIGMA", help="Run sigma command")
sigmacm.set_defaults(func=sigma.run)

# the fflags command
fflagcm = subparsers.add_parser("fflags", help="Add/Remove/View fflags or use fflags preset")
fflagcm.add_argument("view",nargs=argparse.REMAINDER, help="View all fflags")
fflagcm.add_argument("--rm", nargs=argparse.REMAINDER, help="Remove a fflag.")
fflagcm.add_argument("--add",nargs=argparse.REMAINDER, help="Add a fflag")


fflagcm.add_argument("--preset", nargs=argparse.REMAINDER, help="Use fflags preset. Use it to see some preset you can use with")
fflagcm.set_defaults(func=fflags.run)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
