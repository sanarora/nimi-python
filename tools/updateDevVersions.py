# !python

import argparse
import logging
import pprint
import re
import sys

pp = pprint.PrettyPrinter(indent=4, width=100)


def configure_logging(lvl=logging.WARNING, logfile=None):
    root = logging.getLogger()
    root.setLevel(lvl)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(funcName)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S")
    if logfile is None:
        hndlr = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        hndlr = logging.FileHandler(logfile)
    hndlr.setFormatter(formatter)
    root.addHandler(hndlr)


def main():
    # Setup the required arguments for this script
    usage = """
Update version when it is a dev version. I.e. X.Y.Z.devN to X.Y.Z.dev(N+1)
"""
    parser = argparse.ArgumentParser(description=usage)
    file_group = parser.add_argument_group("Input and Output files")
    file_group.add_argument("--src-file", action="store", dest="src_file", default=None, required=True, help="Source file")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument("--exporting", action="store_true", dest="exporting", default=False, help="Are we building an official export? If false, don't actually interact with perforce.")
    verbosity_group.add_argument("-v", "--verbose", action="count", dest="verbose", default=0, help="Verbose output")
    verbosity_group.add_argument("--test", action="store_true", dest="test", default=False, help="Run doctests and quit")
    verbosity_group.add_argument("--log-file", action="store", dest="logfile", default=None, help="Send logging to listed file instead of stdout")
    args = parser.parse_args()

    if args.verbose > 1:
        configure_logging(logging.DEBUG, args.logfile)
    elif args.verbose == 1:
        configure_logging(logging.INFO, args.logfile)
    else:
        configure_logging(logging.WARNING, args.logfile)

    logging.info(pp.pformat(args))

    with open(args.src_file, 'r') as content_file:
        contents = content_file.read()

    version_re = re.compile('(\d+\.\d+\.dev)(\d+)')
    m = version_re.search(contents)
    if m:
        contents = version_re.sub('{0}{1}'.format(m.group(1), int(m.group(2)) + 1), contents)
    else:
        logging.error("no match")

    with open(args.src_file, 'w') as content_file:
        content_file.write(contents)


if __name__ == '__main__':
    main()

