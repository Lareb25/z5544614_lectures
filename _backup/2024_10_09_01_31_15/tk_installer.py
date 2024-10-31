""" tk_utils installer

This module will download and install the `tk_utils` module.

Important
---------

The only purpose of this module is to install the `tk_utils` module.  All you
have to do is to follow the instructions below. 

Do not worry about the content of this module.  

** THIS MODULE INCLUDES MATERIAL WHICH WE WILL NOT COVER IN THIS COURSE **
** THIS MODULE INCLUDES MATERIAL WHICH WE WILL NOT COVER IN THIS COURSE **
** THIS MODULE INCLUDES MATERIAL WHICH WE WILL NOT COVER IN THIS COURSE **

** PLEASE DO NOT MODIFY THIS SCRIPT IN ANY WAY **
** PLEASE DO NOT MODIFY THIS SCRIPT IN ANY WAY **
** PLEASE DO NOT MODIFY THIS SCRIPT IN ANY WAY **

Please follow the instructions below to place this module DIRECTLY under
your `toolkit` project folder:

    toolkit/                    <- PyCharm project root
    |__ ...
    |__ tk_installer.py         <- This module


Quick-guide
-----------

Below is a quick installation guide. If you need more information, see the
"Detailed instructions" section below.

1. Choose your preferred method to place this module directly under `toolkit`

2. Open the Python Console in PyCharm and type

    >>> import tk_installer
    >>> tk_installer.install()

3. You will see a new folder called `tk_utils` under `toolkit`

    toolkit/                    <- PyCharm project root
    |__ ...
    |__ tk_utils/               <- New folder

4. The `tk_utils` module is ready to use. To set it up, type:

    >>> import tk_utils
    >>> tk_utils.setup()

    This will display a series of instructions inside the Python Console

5. Follow the instructions to finish setting up and to learn more about `tk_utils`


Detailed instructions
---------------------

1. Choose ONE of the following approaches to add this module to PyCharm:

    1.1. Drag and drop:

        Drag and drop this module from your favorite file browser 
        (e.g., File Explorer in Windows, Finder in Mac) into PyCharm. 

        Make sure you "drop it" under `toolkit`:

            toolkit/                    <- DROP HERE
            |__ ...
            |__ tk_installer.py         <- THIS FILE WILL APPEAR HERE

    1.2. Copy and paste using your system's file browser:

        a. Right-click on the toolkit project folder and choose `Open in > <BROWSER>`
            where <BROWSER> is your systems file browser.

            Example:

            toolkit/                    <- Right-click here
            |__ ...

            then choose:

                `Open in >> File Explorer`      (in Windows)
                `Open in >> Finder`             (in Mac)

        b. Your file browser will open and you will see a folder called "toolkit"

            Example (inside your file browser):

                .../PyCharmProjects/
                | ...
                |__ toolkit                 <- Open this folder
                | ...

            Note: If you named your PyCharm project something other than
            "toolkit", click on that folder instead

        c. Insider the file browser, You will see all the files included in
           the toolkit folder.  You can then simply copy and paste this file into 
           the toolkit folder (just like you would any other file):

           Example: Suppose you downloaded this module into a folder called 
           "Downloads":


               Open the "Downloads" folder and copy the file

               .../Downloads/
               | ...
               |__ tk_installer.py          <- Copy from here...

               Then open the "toolkit" folder and paste the file

               .../toolkit/
               | ...
               |__ tk_installer.py          <- ... and paste it here


2. Open the Python Console in PyCharm and type

    >>> import tk_installer
    >>> tk_installer.install()

   This will download and install the tk_utils package

    
3. Once completed, you should see the `tk_utils` package inside `toolkit`:    

    toolkit/                    <- PyCharm project root
    |__ ...
    |__ tk_utils/               <- NEW FOLDER (package)
    |__ tk_installer.py         <- This module

   Note: If the installation completed without errors but you do not see the
   new folder inside `toolkit`: Right-click on the `toolkit` project folder
   and choose "Reload from disk"


4. Then go back to the Python Console and type:

    >>> import tk_utils
    >>> tk_utils.setup()     

    This will display a series of instructions inside the Python Console

5. Follow the instructions to finish setting up and to learn more about `tk_utils`


Troubleshooting
---------------

A. Nothing happens after >>> import tk_installer

    a. You need to call the function `.install()` after importing: 

        >>> import tk_installer
        >>> tk_installer.install()

A.  >>> import tk_installer raised an exception, what should I do?

    a. Make sure you spelled the name of the module correctly

    b. Triple check that this module is under the toolkit project folder

        toolkit/                    <- PyCharm project root
        |__ ...
        |__ tk_installer.py         <- This module

    c. Create a new post in ED and include a screenshot of the import error 
    

B. >>> tk_utils.setup() did not do anything, what should I do?

    a. Make sure you typed `tk_utils.setup()` (with parentheses) and NOT
       `tk_utils.setup` (without parentheses)

    b. Make sure you can see the `tk_utils` inside your project folder. 

        toolkit/                    <- PyCharm project root
        |__ ...
        |__ tk_utils/               <- NEW FOLDER (package)
       
    c. Create a new post in ED and include a screenshot of PyCharm

C. >>> import tk_utils raised an exception, what should I do?

    a. Make sure the spelling is correct

    b. Create a new post in ED and include a screenshot of the import error 


         
"""
import requests
import pathlib
import zipfile
import shutil
import datetime as dt
import os
import re
import tempfile
import sys
import textwrap
import importlib
from collections import namedtuple


DROPBOX_URL = 'https://www.dropbox.com/scl/fo/it791t4gsvb275sgkc44m/AHvysANbaep2ZoQl7-Gf4-4?rlkey=t29q4rr4epsjz3538gy3yr49h&st=7j1lokjc&dl=1'
MOD_NAME = 'tk_installer'
PKG_NAME = 'tk_utils'
BASE_TMP_NAME = 'DELETE_ME'
BOLD = "\033[1m"
SEP = '-'*40
NORMAL = "\033[0m"
RQUOTES = re.compile(r'''("|')''')
LOCS_NTUP = namedtuple(
        'Locs', 
        ['prj_root', 'this_dir', 'tmp_zip', 'dbox_url', 'tk_dir', 'tk_dir_bk'])


def _dirtree_msg(
        msg: str,
        branch: str,
        arrow: str,
        ) -> str:
    """ Returns a message with the directory tree"""
    indent = ' '*(24-len(branch))
    return textwrap.dedent(f'''\
    {msg}

        toolkit/                    <- PyCharm project root
        |   ...
        |__ {branch}{indent}<- {arrow}
    ''')

def _chk_importable(name) -> bool:
    """ Returns True if the tk_utils module can be imported
    """
    try:
        mod = importlib.import_module(name)
        return True
    except:
        return False


def _move_children(src: pathlib.Path, dst=pathlib.Path):
    """ Move the elements inside a folder

    Parameters
    ----------
    src: pathlib.Path
        The source folder

    dst: pathlib.Path
        The destination folder (can be inside src)

    """
    if not src.exists():
        raise Exception(f"Path `src` does not exist: '{src}'")
    if not src.is_dir():
        raise Exception(f"Path `src` is not a folder: '{src}'")
    if not dst.exists():
        dst.mkdir(parents=True)
    for pth in src.iterdir():
        if pth == dst or dst.is_relative_to(pth):
            continue
        shutil.move(src=pth, dst=dst)


def ask_yes(msg: str):
    """ Asks for user confirmation and returns True if confirmed.
    Case insensitive.

    Parameters
    ----------
    msg: str
        Message to confirm
    """
    print(f"{BOLD}{msg}{NORMAL}")
    answer = input(f'{BOLD}Please type "YES" to continue or "NO" to exit: {NORMAL}')
    chk_answer = RQUOTES.sub('', answer.lower().strip())
    if chk_answer == 'yes': 
        return True
    elif chk_answer[0] == 'y':
        m = f"You must type 'YES' not '{answer}'. Try again"
        return ask_yes(m)
    else:
        return False


class Installer:
    """ Installation factory

    """

    def __init__(
            self,
            ):
        self.locs = self._mk_locs()
        print(SEP, f"Installing '{PKG_NAME}'...", SEP, sep='\n')

    def _mk_locs(self):
        """ Returns an instance of the locations namedtuple
        """
        prj_root = pathlib.Path(os.getcwd())
        tmp_zip = prj_root.joinpath(BASE_TMP_NAME).with_suffix('.zip')
        tk_dir = prj_root.joinpath(PKG_NAME)
        tk_dir_bk = tk_dir.joinpath(
                '_old', 
                dt.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))

        return LOCS_NTUP(
                prj_root=prj_root,
                this_dir=pathlib.Path(__file__).parent,
                dbox_url=DROPBOX_URL,
                tmp_zip=tmp_zip,
                tk_dir=tk_dir,
                tk_dir_bk=tk_dir_bk,
                )

    def __del__(self):
        self._rm_tmp_zip()

    def _rm_tmp_zip(self):
        """Deletes the temp zip file, if present"""
        if hasattr(self, 'locs') and self.locs.tmp_zip.exists():
            self.locs.tmp_zip.unlink()
        

    def chk_mod_loc(self):
        """ Ensure correct module location"""
        if self.locs.prj_root != self.locs.this_dir:
            err = _dirtree_msg(
                    msg="This module should be placed directly under `toolkit`:",
                    branch=f"{MOD_NAME}.py",
                    arrow="This module")
            raise Exception(err)

    def chk_tk_exists(self):
        """ If package already exists, ask for confirmation"""
        stop = False
        if self.locs.tk_dir.exists():
            msg0 = _dirtree_msg(
                    msg=f"IMPORTANT: The folder `{PKG_NAME}` already exists!",
                    branch=PKG_NAME,
                    arrow="Exists!")
            print(msg0)

            # Check if module can be imported
            msg = "Are you sure you want to delete the folder above and reinstall?"
            if _chk_importable(PKG_NAME):
                msg = f"{msg}\n(You should probably choose NO)"

            res = ask_yes(msg)
            if not res:
                stop = True
            else:
                # Just to be safe, move everything into an _old folder
                _move_children(
                        src=self.locs.tk_dir,
                        dst=self.locs.tk_dir_bk,
                        )
        return stop

    def download(self):
        """Downloads the entire dropbox shared folder into self.locs.tmp_zip"""
        print(f"Downloading '{PKG_NAME}' package...")
        self._rm_tmp_zip()
        r = requests.get(DROPBOX_URL)
        with open(self.locs.tmp_zip, 'wb') as fobj:
            fobj.write(r.content)

    def unzip(self):
        """ Unzip the relevant content from the tmp zip file"""
        print(f"Unzipping file...")
        if not self.locs.tmp_zip.exists():
            err = f"Could not find tmp zip file, try again"
            raise Exception(err)

        with zipfile.ZipFile(self.locs.tmp_zip) as zf:
            for x in zf.namelist():
                if x.startswith(PKG_NAME):
                    zf.extract(x)
        self._rm_tmp_zip()

    def install(self):
        """ Download and installs the tk_utils package"""
        self.chk_mod_loc()
        stop = self.chk_tk_exists()
        if stop:
            print(
                    "Stopping install... Done",
                    sep='\n')
            return
        self.download()
        self.unzip()
        print(
            "Package installed!",
            f"{BOLD}Please type the following to proceed:{NORMAL}",
            f"  >>> import {PKG_NAME}",
            f"  >>> {PKG_NAME}.setup()",
            sep='\n')


def install():
    """ main function"""
    fac = Installer()
    fac.install()


if __name__ == "__main__":
    # Not required but in case they "Run" this module instead of using the
    # Console
    install()








