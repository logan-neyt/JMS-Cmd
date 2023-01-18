#!/usr/bin/env python

import sys


def main():
    arg_pairs, positional_args = __parse_arguments(sys.argv[1:])
    
    for help_arg in ['h', 'help', '?']:
        if help_arg in arg_pairs.keys():
            __print_help(positional_args + arg_pairs[help_arg])
    
    # TODO MQ Connection

    # TODO Action based on positional arg


def __print_help(positional_args: list[str] = None):
    if positional_args == None or isinstance(positional_args[0], bool): # There will always at least be an argument from the help argument (implicitly a boolean True).
        # TODO Write usage help
        print(
"""JMS Command Line Tools

Available sub-commands:
    browse
    listen
    send
    list
""")

    else:
        match positional_args[0]:
            case 'browse':
                # TODO Write help
                print("""TODO Write browse help""")
            case 'listen':
                # TODO Write help
                print("""TODO Write listen help""")
            case 'send':
                # TODO Write help
                print("""TODO Write send help""")
            case 'list':
                # TODO Write help
                print("""TODO Write list help""")
            case _:
                print("No help entry for \"" + positional_args[0] + "\"")
    
    sys.exit(0)


def __parse_arguments(raw_args: list[str]):
    arg_pairs: dict[str, list[Union(str, int, bool)]] = {}
    positional_args: list[str] = []

    key: str = None
    for argument in raw_args:
        if key != None:
            if argument[0] == '-':  # Eg: -a -b
                __add_to_arg_pairs(arg_pairs, key, True)
                key = None
            else:
                __add_to_arg_pairs(arg_pairs, key, argument)
                key = None
                continue
            
        if argument[0] == '-':
            if len(argument) == 1:   # Eg: -
                raise Exception("Invalid argument \"" + argument + "\"")

            if argument[1] == '-':  # Eg: Long argument
                if len(argument) == 2:
                    raise Exception("Invalid argument \"" + argument + "\"")

                if '=' in argument: # Eg: --key=value
                    argument_parts = argument.split('=')
                    __add_to_arg_pairs(arg_pairs, argument_parts[0][2:], '='.join(argument_parts[1:]))
                else:   # Eg: --key value
                    key = argument[2:]

            else:
                if len(argument) > 2:  # Eg: -abcd
                    for flag in argument[1:-1]:
                        __add_to_arg_pairs(arg_pairs, flag, True)
                key = argument[-1]

        else:   # Positional argument, Eg: posArg1 posArg2
            positional_args.append(argument)

    if key != None: # If last argument is a flag
        __add_to_arg_pairs(arg_pairs, key, True)

    return arg_pairs, positional_args


def __add_to_arg_pairs(dictionary: dict[str, list[str]], key: str, value: str = None) -> None:
    if key == None or key == '':
        raise Exception("Invalid argument \"" + key + "\"") 
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]


if __name__ == '__main__':
    main()