import argparse
import os
import sys

from lang import logger, lang

sys.path.append(os.path.dirname("."))


def main():
    """main"""
    parser = argparse.ArgumentParser(
        prog="lang-py",
        description="lang-py",
        epilog='Text at the bottom of help'
    )
    parser.add_argument(
        '-d', '--debug',
        type=bool, default=False,
        required=False,
    )
    parser.add_argument(
        'path',
        type=str, default='',
    )
    args = parser.parse_args()
    logger.debug("args:", args)

    if args.debug:
        logger.set_debug()

    if not args.path:
        logger.info(parser.format_help())
        exit(0)

    lang.execute(args.path)


if __name__ == "__main__":
    main()
