from modules.json.json import ReadSoberConfig
import json

def run(args):
    if args.view :
        print("All fflags in config.json :")
        fflagscf = ReadSoberConfig("fflags")
        pretty = json.dumps(fflagscf,indent=4)
        print(pretty)
    else:
        print("Type help to see how to use fflag command")