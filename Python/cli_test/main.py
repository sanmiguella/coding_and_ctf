import sys

class Text_Manipulator:
    @classmethod
    def get_options_and_args(cls):
        # If it starts with '-' , then it will be an option, else it will be an argument.
        opts = [opt.lower() for opt in sys.argv[1:] if opt.startswith("-")]
        args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

        return opts, args

    @classmethod
    def show_help(cls):
        # Use '\' as delimeter and get the last element of the list.
        prgName = sys.argv[0].split("\\")[-1]

        message = "\n"
        message += "There can be any number of arguments but,\n"
        message += "Only 1 of the 3 options are allowed:\n\n"
        message += " -c/-C, --cap (Capitalize)\n"
        message += " -u/-U, --upper (UPPERCASE)\n"
        message += " -l/-L, --lower (lowercase)\n\n"
        message += "Program usage:\n\n"
        message += f" {prgName} (-c | -u | -l) <arguments>\n"
        message += f" {prgName} (--cap | --upper | --lower) <arguments>"

        raise SystemExit(message)

    @classmethod
    def process_options_and_args(cls, opts, args):
        if "-c" in opts or "--cap" in opts: # Capitalized
            # Capitalize every element, 
            # Make that element a member of another list,
            # Joins the said list into a string.
            print(f"[+] Results capitalized - {' '.join([arg.capitalize() for arg in args])}")
    
        elif "-u" in opts or "--upper" in opts: # Uppercase
            print(f"[+] Results uppercase - {' '.join([arg.upper() for arg in args])}")

        elif "-l" in opts or "--lower" in opts: # Lowercase
            print(f"[+] Results lowercae - {' '.join([arg.lower() for arg in args])}")

        else:
            cls.show_help()

    @classmethod
    def execute(cls):
        opts, args = cls.get_options_and_args()
        cls.process_options_and_args(opts, args)

Text_Manipulator.execute()