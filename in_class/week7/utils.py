""" Utilities for Week 7 lectures

This module implements helper functions

         
"""

import pprint as pp

import pandas as pd

def printit(*args, 
            add_sep = False,
            show_type = False,
            show_id = False,
            pretty: bool = False,
            width: int = 40,
            ):
    """ Helper print function. Call the function `print` but add separators

    Parameters
    ----------
    *args:
        Objects to be printed. Each object will be printed in a separate line.

    add_sep: bool, default False
        If True, add line separators before and after the objects to be
        printed

    show_type: bool, default False
        If True, print the type of any object which is not a str instance

    show_id: bool, default False
        If True, display id(obj)  for all objects with are not a string.

    pretty: bool, default False
        If True, use pretty printer to print non-string objects

    """
    new_args = []

    if pretty is True:
        # Pandas use its own pretty printer
        # Save the original width
        pd_width = pd.get_option('display.width')

        # Then set the new width
        pd.options.display.width = width

    # Add pandas/other types if required
    nargs = len(args)
    for i, arg in enumerate(args):
        if pretty is False or isinstance(arg, str):
            new_args.append(arg)
        else:
            new_args.append(pp.pformat(arg, width=width))

        if not isinstance(arg, str):
            to_add = []
            if show_type is True:
                to_add.append(f"Type: {type(arg).__name__}")
            if show_id is True:
                to_add.append(f"ID: {id(arg)}")
            if len(to_add) > 0:
                # Add an empty line
                new_args.append('')
                new_args.extend(to_add)
                # If this is not the last argument, add an empty line
                if i < nargs:
                    new_args.append('')

    if add_sep is True:
        line_sep = '-' * 40
        new_args.insert(0, line_sep)
        new_args.append(line_sep)

    # Revert pandas display width
    if pretty is True:
        pd.options.display.width = pd_width

    print(*new_args, sep='\n')

