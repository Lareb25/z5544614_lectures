""" The tk_utils package

PLEASE DO NOT MODIFY THIS FILE
PLEASE DO NOT MODIFY THIS FILE
PLEASE DO NOT MODIFY THIS FILE
PLEASE DO NOT MODIFY THIS FILE
"""
import pathlib
import sys as _sys


try:
    from _tk_utils import *
except (ImportError, ModuleNotFoundError):
    _tk_root = pathlib.Path(__file__).resolve().parent
    _tk_utils_zip = _tk_root.joinpath('_tk_utils.zip')
    if _tk_utils_zip.exists():
        _sys.path.insert(0, str(_tk_utils_zip))
        from _tk_utils import *
    else:
        from ._tk_utils import *



# Get all module-level functions
_funcs = [
        pd.read_csv_str,
        #colorize,
        backup,
        sync_dbox,
        ]
# Get all sub-packages

__doc__ = docs.mk_tk_utils_doc(funcs=_funcs)


