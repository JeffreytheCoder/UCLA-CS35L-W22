#!/usr/bin/env python
import sys
import argparse
import random


def parse_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    return lines


def parse_lo_hi(lo_hi):
    lo, hi = lo_hi.split("-")
    return (int(lo), int(hi))


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-e", "--echo", action="store_true",
                        help="Treat each command-line operand as an input line.")

    parser.add_argument("-i", "--input-range", metavar="LO-HI",
                        help="Act as if input came from a file containing the range of unsigned decimal integers lo...hi, one per line")

    parser.add_argument("-n", "--head-count", metavar="COUNT", action="store", type=int,
                        help="Output at most count lines. By default, all input lines are output.")

    parser.add_argument("-r", "--repeat", action="store_true",
                        help="Repeat output values, that is, select with replacement. With this option the output is not a permutation of the input; instead, each output line is randomly chosen from all the inputs.")

    parser.add_argument("-", "--read-stdin",
                        action="store_true", help="read standard input file")

    options, args = parser.parse_known_args(sys.argv[1:])
    print(options)

    for arg in args:
        if arg[0] == '-':
            sys.stdout.write(
                "shuf: invalid option -- " + arg[1] + "\nTry 'shuf --help' for more information.\n")
            exit(0)

    match True:
        case options.echo:
            lines = args

        case _:
            if options.input_range:
                lo, hi = parse_lo_hi(options.input_range)
                lines = [str(x) for x in range(lo, hi + 1)]
                         
            elif len(args) > 0:
                lines = parse_file(args[0])
                
            else:
                lines = []
                while True:
                    try:
                        line = input()
                        lines.append(line + '\n')
                    except EOFError:
                        break

    count = len(lines)
    if options.head_count:
        count = options.head_count
        
    count = min(len(lines), count)
    
    try:
        if options.repeat:
            count_down = options.head_count
            while True:
                for line in random.sample(lines, count):
                    sys.stdout.write(line.rstrip('\n') + '\n')
                    
                    if options.head_count:
                        count_down -= 1
                    
                    if count_down == 0:
                        break
                
                if count_down == 0:
                        break

        else:
            for line in random.sample(lines, count):
                sys.stdout.write(line.rstrip('\n') + '\n')

    except Exception as err:
        parser.error("I/O error({0}): {1}".format(err))
        exit(0)



if __name__ == "__main__":
    main()
