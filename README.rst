===============================================
PyNaCl: Python binding to the libsodium library
===============================================

OSX Compilation
--------------------

This process must be done with a Mac.

**Step 1**: Create a virtual environment:

::

    $ python -m venv venv

**Step 2**: Access to the virtual environment and compile Libsodium:

::

    $ venv
    $ python setup.py bdist_wheel

Now, you should see a **dist** folder that contains a file like the following one: `PyNaCl-1.5.0.dev1-cp38-cp38-win_amd64.whl`. This is the file that must be installed. Note that it contains the Python version, which means that a new compilation is required for each Python version.


Windows Compilation
--------------------

This process must be done with a Windows.

**Step 1**: Create a virtual environment:

::

    $ python -M venv venv

**Step 2**: Download the latest Libsodium MSVC from the following URL: `https://download.libsodium.org/libsodium/releases/`. At the time of writing it is the file `libsodium-1.0.18-msvc.zip`.

**Step 3**: Extract the downloaded file and place it in a location you won't delete. In our case is at C:\\libsodium, where we have the following directories (may vary, depends on the version):

- C:\libsodium\include
- C:\libsodium\Win32
- C:\libsodium\x64

**Step 4**: Install the `make` command for Windows. For this, we will use the dependency manager `choco`. Install it if you haven't already. The following command should be executed with Administration privileges:

::

    $ choco install make

Ensure it is installed. Open a new CMD and type `where make` or `make` to ensure it is found.

**Step 5**: Select the Windows release for compilation. They can be found at `C:\\libsodium\\x64\\Release` (depends on where you installed the libsodium). Each `VXXX` folder, for example `V140`, represents a Windows version. For example, V120 is Windows7 and V14X is Windows 10. To go safe, choose the one with the highest number (at the time of writing is `C:\\libsodium\\x64\\Release\\v142`). From now on, we will reference this directory as WINDOWS_RELEASE.

**Step 6**: Compile the binary (change `WINDOWS_RELEASE` for the path selected in the previous step):

::

    @set SODIUM_INSTALL=system
    @set PYNACL_SODIUM_STATIC=1
    @set LIB="WINDOWS_RELEASE";%LIB%
    @set INCLUDE="C:\libsodium\include";%INCLUDE%
    python setup.py bdist_wheel

If you find the error `ERROR: The 'make' utility is missing from PATH`, it means the make command cannot be executed. If you open the CMD and type `make` and it does work, modify the Python function that raises this error and make it work (we had to do this already).
Now, you should see a **dist** folder that contains a file like the following one: `PyNaCl-1.5.0.dev1-cp38-cp38-win_amd64.whl`. This is the file that must be installed. Note that it contains the Python version, which means that a new compilation is required for each Python version.

**Step 7**: The wheel file that has been created in the **dist** directory must be unpacked to add a file. Open the terminal with the virtual environment and:

1. wheel unpack dist/PyNaCl-1.5.0.dev1-cp38-cp38-win_amd64.whl
2. Inside the unpacked wheel directory, go to the `nacl` directory and ensure the file libsoidum.dll and libsodium.lib exists. If not, copy all the files from `C:\\libsodium\\x64\\Release\\WINDOWS_RELEASE\\dynamic`, for example `C:\\libsodium\\x64\\Release\\v142\\dynamic`.
3. wheel pack PyNaCl-1.5.0.dev1
4. Replace the wheel in dist/ with the new one.

**Final notes**: When you install the wheel on Windows, if the error `ImportError: DLL load failed` pops up when importing nacl._sodium:

1. Download the dependency analyzer from: https://github.com/lucasg/Dependencies
2. Open the dependency analyzer as GUI
3. Load the _sodium.pyd file from the installed wheel. In our case is at `venv/Lib/site-packages/nacl/_sodium.pyd`
4. Ensure all the dependencies are right. If libsodium.lib or libsodium.dll is missing, go back to step 7.