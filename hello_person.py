# command line arguments are like poor mans SSH
# when yo see words spaced apart, that is a command

def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }

    msg = f"{greetings[lang]} {name}"
    print(msg)

import argparse

parser = argparse.ArgumentParser(
    description="Provides a personal greeting."
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of the person to greet."
)

parser.add_argument(
    "-l", "--lang", metavar="language", required=True,
    choices=["English", "Spanish", "German"],
    help="The language of the greeting"
)
args = parser.parse_args()

mesg = f"Hello {args.name}!"
print(mesg)

