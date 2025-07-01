from modules.json.json import ReadSoberConfig, UpdateFflags, DeleteFflag
import json

def run(args):
    if args.view :
        print("All fflags in config.json :")
        fflagscf = ReadSoberConfig("fflags")
        pretty = json.dumps(fflagscf,indent=4)
        print(pretty)
    
    if arg.rm :
        fflag = args[0]
        print(f"Deleting {fflag}")
        DeleteFflag(fflag)

    if args.add is None or len(args.add) == 0: # if nothing retrun usage
        print("Usage: --add [fflag] [Value]")
        return
    
    if len(args.add) >= 2:
        fflag = args.add[0]
        value = args.add[1]
        print(f"debug fflag: {fflag} = {value}")
        UpdateFflags(fflag, value)
        return


print("Type help to see how to use fflag command")