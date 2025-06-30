import sys

class LutionCLI:
    def __init__(self, command=None, args=None):
        self.command = command
        self.args = args or []

    def run(self):
        match self.command:
            case "test":
                self.test_command()
            case _:
                print("unknown command")

    def test_command(self):
        print("test!")
        print("extra args:", self.args)

def main():
    args = sys.argv[1:]  # skip script name
    command = args[0] if args else None
    extra_args = args[1:] if len(args) > 1 else []
    cli = LutionCLI(command, extra_args)
    cli.run()

if __name__ == "__main__":
    main()
