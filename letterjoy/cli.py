import argparse
import sys

from letterjoy.ciphers import polysubstitution


def main():
    parser = argparse.ArgumentParser(
        prog="letterjoy",
        description="Encode or decode Letterjoy subscription ciphers.",
    )

    # Cipher type — mutually exclusive so new cipher types can be added later
    cipher_group = parser.add_mutually_exclusive_group(required=True)
    cipher_group.add_argument(
        "--polysubstitution",
        action="store_true",
        help="Polyalphabetic substitution cipher (period = number of key rows).",
    )

    # Direction
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("--encode", action="store_true", help="Encode the message.")
    mode_group.add_argument("--decode", action="store_true", help="Decode the message.")

    # Key file
    parser.add_argument(
        "--cipherkey",
        required=True,
        metavar="FILE",
        help="Path to the cipher key file.",
    )

    # Message input — file argument, --message flag, or stdin
    input_group = parser.add_mutually_exclusive_group()
    input_group.add_argument(
        "--message",
        metavar="TEXT",
        help="Message text to process (quoted string).",
    )
    input_group.add_argument(
        "message_file",
        nargs="?",
        metavar="FILE",
        help="File containing the message to process.",
    )

    args = parser.parse_args()

    # Resolve message from the three possible sources
    if args.message:
        message = args.message
    elif args.message_file:
        with open(args.message_file) as f:
            message = f.read()
    elif not sys.stdin.isatty():
        message = sys.stdin.read()
    else:
        parser.error(
            "Provide a message via --message TEXT, a file argument, or pipe via stdin."
        )

    # Load key and run the selected cipher
    key_rows = polysubstitution.load_key(args.cipherkey)

    if args.polysubstitution:
        if args.decode:
            result = polysubstitution.decode(message, key_rows)
        else:
            result = polysubstitution.encode(message, key_rows)

    print(result)


if __name__ == "__main__":
    main()
